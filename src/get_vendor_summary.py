from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Engine setup
engine = create_engine(
    "mysql+pymysql://root:76543210@localhost:3306/inventory"
)

def create_vendor_summary(engine):
    """Merge tables to create vendor sales summary"""
    
    logging.info('Starting vendor summary creation')

    vendor_sales_summary = pd.read_sql_query(
        '''WITH FreightSummary AS (
            SELECT VendorNumber, SUM(Freight) AS FreightCost
            FROM vendor_invoice
            GROUP BY VendorNumber
        ),
        PurchaseSummary AS (
            SELECT
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price AS ActualPrice,
                pp.Volume,
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Dollars) AS TotalPurchaseDollars
            FROM purchases p
            JOIN purchase_prices pp ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY
                p.VendorNumber, p.VendorName, p.Brand, p.Description,
                p.PurchasePrice, pp.Price, pp.Volume
        ),
        SalesSummary AS (
            SELECT
                VendorNo,
                Brand,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(SalesDollars) AS TotalSalesDollars,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            GROUP BY VendorNo, Brand
        )
        SELECT
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss
            ON ps.VendorNumber = ss.VendorNo AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
        ''',
        engine
    )

    logging.info(
        'Vendor summary fetched: %d rows',
        len(vendor_sales_summary)
    )

    return vendor_sales_summary



def clean_data(df):
    '''This function will clean the data'''
    #changing datatypes
    df['Volume'] = df['Volume'].astype('float64')
    df['TotalPurchaseQuantity'] = (df['TotalPurchaseQuantity'].fillna(0).astype(int))
    df['TotalSalesQuantity'] = (df['TotalSalesQuantity'].fillna(0).astype(int))

    #removing spaces from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    #Creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']

    df['ProfitMargin'] = (df['GrossProfit'] /df['TotalSalesDollars'].replace(0, np.nan)) * 100

    df['StockTurnover'] = ( df['TotalSalesQuantity'] / df['TotalPurchaseQuantity'].replace(0, np.nan)
    )

    df['SalestoPurchaseRatio'] = (df['TotalSalesDollars'] /df['TotalPurchaseDollars'].replace(0, np.nan))

    #Filling Missing Values with 0

    df.fillna(0, inplace=True)
    return df


    
if __name__ == '__main__':

    logging.info('Creating Vendor Summary Table.....')
    summary_df = create_vendor_summary(engine)
    logging.info(summary_df.head())

    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.....')
    ingest_db(clean_df, 'vendor_sales_summary', engine)
    logging.info('Completed')

    
    
    
    





