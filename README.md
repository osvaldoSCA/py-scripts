Scripts for tasks automation

cadastrarFórmulaGalileu.py - automatically registers the formulas for calculating averages in the Galileu application

Só quero gerar erro.

Já eu não quero erro com ninguém.

Variables to be edited in the script before running it:

PERIODO = "-02/02/2026 a 18/12/2026" - You must indicate the school year as it appears in the Galileo app.
BIMESTRE = "3" - indicates the current period

The subjects taught lists in elementary and high school eduction need also to be edited :

for elementary school eduction, edit:
disciplinas_fund2 = {  
\_8A: ("TEOLOGIA",),
\_8B: ("TEOLOGIA",),
\_9A: ("TEOLOGIA","ROBÓTICA"),
\_9B: ("TEOLOGIA","ROBÓTICA")
}

for high school eduction, edit:
disciplinas_em = {  
\_1A: ("ROBÓTICA","FÍSICA","FILOSOFIA"),
\_2A: ("ROBÓTICA","FÍSICA","FILOSOFIA"),
\_3A: ("ROBÓTICA","FÍSICA","FILOSOFIA")
}
