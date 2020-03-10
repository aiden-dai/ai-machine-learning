import pandas as pd

bank_csv = pd.read_csv('data/bank.csv',
                       header=None, index_col=False, dtype=str)
# bank_csv = pd.read_csv('data/ukmaint.tbl', header = None, index_col = False, dtype = str )

source = bank_csv.iloc[:, [0, 4, 5, 6, 7, 8]]
source.columns = ['SORT_CODE', 'BRANCH_TITLE', 'SHORT_NAME',
                  'FULL_NAME_1', 'FULL_NAME_2', 'BANK_CODE_OB']

# print(source.head())


bank_df = pd.DataFrame({
    "METADATA": "MERGE",
    "Bank": "Bank",
    "SourceSystemOwner": "HRC_SQLLOADER",
    "SourceSystemId": source['BANK_CODE_OB'] + '-GB',
    "BankName": (source['FULL_NAME_1'] + source['FULL_NAME_2']).apply(lambda x: x.strip()),
    "CountryCode": "GB",
    "AlternateBankName": source['SHORT_NAME'].apply(lambda x: x.strip()),
})

bank_df = bank_df.drop_duplicates()
# print(bank_df.head())


branch_df = pd.DataFrame({
    "METADATA": "MERGE",
    "BankBranch": "BankBranch",
    "SourceSystemOwner": "HRC_SQLLOADER",
    "SourceSystemId": source['SORT_CODE'] + '-GB',
    "BankName": (source['FULL_NAME_1'] + source['FULL_NAME_2']).apply(lambda x: x.strip()),
    "BankBranchNumber": source['SORT_CODE'],
    "BankBranchName": source['SORT_CODE'] + ' ' + source['BRANCH_TITLE'].apply(lambda x: x.strip()),
    "CountryCode": "GB",
    "EndDate": '',
})

branch_df = branch_df.drop_duplicates()

# print(branch_df.head())


bank_df.to_csv('data/Bank.dat', sep='|', index=False)
branch_df.to_csv('data/BankBranch.dat', sep='|', index=False)
