import pandas as pd

dados = [
    ["G4-Helielton💯",1,"67%","—",23597],
    ["G3-limasxz",2,"61%","—",20483],
    ["G5-kauan-DG RED",3,"61%","—",20118],
    ["G4 joao marcos",4,"61%","—",19825],
    ["G-2 Davizinho",5,"61%","—",19334],
    ["G-3 Igor",6,"61%","—",18958],
    ["G-04 isnaele",7,"64%","—",18646],
    ["G5-Hemerson",8,"58%","—",17530],
    ["G2-Thauan",9,"50%","—",17027],
    ["G1-joãoelias",10,"56%","—",16689],
    ["G-4=ADRIAN",11,"53%","—",16499],
    ["G-2 RENAN",12,"53%","—",16283],
    ["G-04👿Jvn👺👿",13,"58%","—",16082],
    ["G5-Wilsonir",14,"53%","—",16078],
    ["G-2 zidane",15,"56%","—",15724],
    ["G-6 YASLEY",16,"47%","—",14815],
    ["G-4 Jefferson",17,"50%","—",14474],
    ["G2-MOISÉS",18,"50%","—",14115],
    ["G1-TheAlef😎",19,"44%","—",13817],
    ["G-6 VANI",20,"44%","—",12584],
    ["G-3Newtton",21,"42%","—",12268],
    ["G-6 Gabriel",22,"47%","—",12089],
    ["G-6ariel",23,"31%","—",9178],
    ["G1_amparo",24,"31%","—",9004],
    ["G3-Fernanda",25,"28%","—",7110],
    ["G-6 Anderson",26,"14%","—",4804],
]

df = pd.DataFrame(
    dados,
    columns=[
        "Apelido",
        "Classificação",
        "Respostas corretas",
        "Não respondido",
        "Pontuação final",
    ],
)

print(df.to_string(index=False))

csv_path = "resultado_kahoot.csv"
xlsx_path = "resultado_kahoot.xlsx"

df.to_csv(csv_path, index=False)

with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Resultados")

print(f"\nCSV salvo em: {csv_path}")
print(f"Excel salvo em: {xlsx_path}")