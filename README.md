# GS_2_SERS
Sistema de Monitoramento e Simulação Energética para Ambientes de Trabalho

Este repositório apresenta um sistema completo em Python voltado para análise, simulação e automação energética em ambientes de trabalho modernos.
O objetivo é apoiar a transição para modelos de trabalho mais sustentáveis, reduzindo custos, aumentando a eficiência e incentivando o uso de energias renováveis no contexto corporativo.

O sistema integra:

Simulação de consumo energético em um ambiente de trabalho

Detecção inteligente de picos

Modelagem de geração solar

Comportamento IoT simulado para alertas

Base para automação e sustentabilidade no futuro do trabalho

Descrição da Solução

O sistema é organizado em quatro módulos principais que representam elementos essenciais da gestão energética corporativa.

1) data_gen.py — Gerador de Dados de Consumo em Ambientes de Trabalho

Gera um conjunto de dados sintético representando o consumo de energia de um ambiente produtivo ao longo do dia, simulando:

Períodos de maior atividade (horário comercial)

Equipamentos ligados simultaneamente

Variações naturais no uso de energia

Produz o arquivo energia.csv, utilizado por todo o restante do projeto.

2) analysis.py — Análise de Consumo e Identificação de Picos

Realiza:

Limpeza e leitura dos dados

Cálculo de média móvel

Detecção de picos estatísticos (z-score) que podem indicar:

Sobrecarga de equipamentos

Uso ineficiente

Desperdícios invisíveis

Gera:

Gráficos de análise

O arquivo consumo_com_peaks.csv com sinalização de horas críticas

3) simulation_solar.py — Simulação de Geração Solar em Instalações Corporativas

Modela um sistema fotovoltaico aplicado ao ambiente de trabalho analisado, permitindo estimar:

Quanto da demanda poderia ser suprida por energia renovável

Horas de excedente energético

Horas de déficit

Potencial de economia energética

A saída é consumo_com_pv.csv, além de gráficos comparativos.

4) iot_simulator.py — Monitoramento Inteligente Estilo IoT

Simula o comportamento de um dispositivo IoT corporativo capaz de:

Analisar em tempo real os dados simulados

Identificar condições críticas

Emitir alertas, como:

“Consumo acima da capacidade do sistema solar”

“Pico de uso detectado”

“Geração solar insuficiente”

Esse módulo representa o início de uma automação energética real para ambientes de trabalho.

Estrutura do Projeto
energia-futuro-trabalho/
│
├── data/
│   ├── energia.csv
│   ├── consumo_com_peaks.csv
│   └── solar_simulation.csv
│
├── src/
│   ├── data_gen.py
│   ├── analysis.py
│   ├── simulation_solar.py
│   └── iot_simulator.py
│
└── README.md

Como Executar
Pré-requisitos

Python 3.10+

Instalar dependências:

pip install pandas numpy matplotlib

1) Gerar dados de consumo corporativo
python src/data_gen.py --out data/energia.csv

2) Analisar o consumo e detectar picos
python src/analysis.py --in data/energia.csv --out data/

3) Simular sistema solar no ambiente de trabalho
python src/simulation_solar.py --consumo data/consumo_com_peaks.csv --out data/

4) Simular comportamento IoT
python src/iot_simulator.py --in data/solar_simulation.csv

Aplicação no Contexto do Futuro do Trabalho

Este projeto permite desenvolver soluções sustentáveis aplicáveis a ambientes de trabalho modernos:

Otimização automática de uso de energia

Identificação de desperdícios e gargalos

Planejamento de sistemas solares corporativos

Uso de IoT para decisões inteligentes em tempo real

Criação de ambientes produtivos mais eficientes e ecológicos

Base para automações energéticas com impacto direto em custos operacionais

Pode ser expandido para baterias corporativas, políticas de deslocamento de carga, predição de consumo com IA, dashboards em tempo real e automação de equipamentos.
