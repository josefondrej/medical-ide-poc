from pandas import read_excel, set_option

set_option("display.max_columns", 20)
set_option("display.width", 500)
catalogue_path = "SwissDRG-Version_10_0_Fallpauschalenkatalog_AV_2021_2021.xlsx"
df = read_excel(catalogue_path, sheet_name="Akutspitäler", skiprows=7)
df = df.iloc[:, [0, 2]]
df.columns = ["code", "text"]
df.set_index("code", inplace=True)

code_to_text = df["text"].to_dict()
code_text = [[key, value] for key, value in code_to_text.items()]

print(code_text)
