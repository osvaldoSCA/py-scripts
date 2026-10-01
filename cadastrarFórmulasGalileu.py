from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

ATIVIDADE = "MEDIA"

PERIODO = "-02/02/2026 a 18/12/2026"

FUNDII = "-- ENSINO FUNDAMENTAL II"
MEDIO = "-- ENSINO MÉDIO"

_8A = "8\u00baA-8\u00ba ANO"+PERIODO
_8B = "8\u00baB-8\u00ba ANO"+PERIODO
_9A = "9\u00baA-9\u00ba ANO"+PERIODO
_9B = "9\u00baB-9\u00ba ANO"+PERIODO
_1A = "1\u00aaA-1\u00aa SÉRIE"+PERIODO
_2A = "2\u00aaA-2\u00aa SÉRIE"+PERIODO
_3A = "3\u00aaA-3\u00aa SÉRIE"+PERIODO

# dicionário de disciplinas por turma
disciplinas_fund2 = {
    _8A: ("TEOLOGIA",),
    _8B: ("TEOLOGIA",),
    _9A: ("TEOLOGIA","ROBÓTICA"),
    _9B: ("TEOLOGIA","ROBÓTICA")
    }
disciplinas_em = {
    _1A: ("ROBÓTICA","FÍSICA","FILOSOFIA"),
    _2A: ("ROBÓTICA","FÍSICA","FILOSOFIA"),
    _3A: ("ROBÓTICA","FÍSICA","FILOSOFIA")
}
disciplinas = {
    FUNDII: disciplinas_fund2,
    MEDIO: disciplinas_em
}

BIMESTRE = "3"
BIMESTRE_KEY = BIMESTRE+"\u00ba Bimestre"

driver = webdriver.Chrome()

driver.get("https://appgalileu.com.br/professor")

usuario = driver.find_element(By.ID, "identity")
senha = driver.find_element(By.ID, "credential")

usuario.send_keys("sementes_mafra")
senha.send_keys("l@udatoS1")

driver.find_element(By.ID, "btn-entrar").click()

time.sleep(1)

# Ensino Fundamental
for cursoKey in disciplinas.keys():
    for turmaKey in disciplinas[cursoKey].keys():
        for disciplinaKey in disciplinas[cursoKey][turmaKey]:
            #print("cursoKey: "+cursoKey)
            #print("turmaKey: "+turmaKey)
            #print("disciplinaKey: "+disciplinaKey)
            #print("bimestreKey: "+BIMESTRE_KEY)
            driver.get("https://appgalileu.com.br/professor/criterio-avaliacao-periodo")
            time.sleep(1)
            driver.find_element(By.ID, "btnNovo").click()
            time.sleep(1)
            curso = Select(driver.find_element(By.ID, "id_curso"))
            turma = Select(driver.find_element(By.ID, "id_turma"))
            disciplina = Select(driver.find_element(By.ID, "id_disciplina"))
            periodo = Select(driver.find_element(By.ID, "nr_periodo"))
            curso.select_by_visible_text(cursoKey)
            time.sleep(1)
            turma.select_by_visible_text(turmaKey)
            time.sleep(1)
            disciplina.select_by_visible_text(disciplinaKey)
            time.sleep(1)
            periodo.select_by_visible_text(BIMESTRE_KEY)
            time.sleep(1)

            #criar atividade
            driver.find_element(By.ID, "btn-add-atividade").click()
            time.sleep(1)
            driver.find_element(By.ID, "atividade-tx_nomeatividade").send_keys(ATIVIDADE)
            time.sleep(1)
            driver.find_element(By.ID, "btnConfirmarAtividadeGrupo").click()
            time.sleep(1)

            # completar fórmula e salvar
            driver.find_element(By.ID, "criterio-tx_formula").send_keys(ATIVIDADE)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            driver.find_element(By.ID, "btnSalvar").click()
            time.sleep(5)
            