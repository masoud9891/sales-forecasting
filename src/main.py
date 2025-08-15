from data_loader import load_sales_data

def main():
    df = load_sales_data
    print("Data Preview:")
    print(df.head())

if __name__ == "__main__":
    main()