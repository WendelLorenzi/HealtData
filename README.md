# HealtData

<p>&nbsp; Software que combina dados de SRAG (Sindrome Respiratória Aguda Grave) e Clima (Temperatura e Umidade) de determinadas regiões. 
Utilizando de datasets disponibilizados pelo [DATASUS](https://opendatasus.saude.gov.br/dataset?q=SRAG&sort=score+desc%2C+metadata_modified+desc) e [INMET](https://bdmep.inmet.gov.br/),
foi desenvolvido um programa que realiza uma pesquisa em tempo real com base na média diaria de temperatura e umidade utilizando da equação de média aritmética (Xn/n).<br>
O software solicita como atributos para entrada de dados, genero, idade e região, ou seja, o usuário tem de preencher tais informações para que o programa realize a analise e retorne os graficos informativos.</p>

<p> &nbsp; Tal pesquisa consiste em uma análise de 10 (dez) anos de registros do SUS (Sistema Único de Saúde) e torres metereológicas do INMET (Instituto Nacional de Metereologia).
Com base neses dados, foi realizado uma filtragem e normalização dos mesmos para que a análise seja efetuada com precisão.</p>

![telaHeltData](https://user-images.githubusercontent.com/38894557/147290689-5a0b8c93-165c-48a5-9823-448ca97eabb5.png)


