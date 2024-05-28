# Instruções para rodar o app:
# 1. Instale o Streamlit: pip install streamlit
# 2. Salve este arquivo como streamlit_app.py
# 3. Rode o aplicativo com: streamlit run streamlit_app.py

import streamlit as st 

st.title("Checklist - Crédito Comercial")

# Inicializar session_state para controlar o menu e a seleção dos apêndices
if 'menu' not in st.session_state:
    st.session_state.menu = 'principal'
if 'apendice_selecao' not in st.session_state:
    st.session_state.apendice_selecao = None

# Função para exibir o menu principal
def mostrar_menu_principal():
    st.session_state.menu = 'principal'
    st.experimental_rerun()

# CSS para estilizar os botões
def get_button_css(selected):
    return f"""
    <style>
        .stButton>button {{
            background-color: #f0f0f0;
            color: black;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            width: 200px; /* Largura fixa */
        }}
        .stButton>button:hover {{
            background-color: #ddd;
        }}
        .stButton>button.selected {{
            background-color: #4CAF50;
            color: white;
        }}
        .menu-title {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .button-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }}
    </style>
    <script>
        function updateButtonStyles() {{
            let buttons = document.querySelectorAll('.stButton>button');
            buttons.forEach(button => {{
                if (button.innerText === '{selected}') {{
                    button.classList.add('selected');
                }} else {{
                    button.classList.remove('selected');
                }}
            }});
        }}
        document.addEventListener('DOMContentLoaded', updateButtonStyles);
        document.addEventListener('click', updateButtonStyles);
    </script>
    """

def main():
    # Adiciona o CSS aos botões
    selected_button = st.session_state.menu
    st.markdown(get_button_css(selected_button), unsafe_allow_html=True)
    
    # Verificar qual menu exibir
    if st.session_state.menu == 'principal':
        # Título do menu principal
        st.markdown("<p class='menu-title'>Selecione uma opção:</p>", unsafe_allow_html=True)
        
        # Organizando os botões em uma grade centralizada
        col1, col2, col3, col4, col5 = st.columns(5)

        # Adicionando botões centralizados em cada coluna
        with col1:
            st.markdown(get_button_css(''), unsafe_allow_html=True)
            acolhimento_proposta = st.button("Acolhimento Proposta", key="acolhimento_proposta", help="Acolhimento Proposta")
            
        with col2:
            st.markdown(get_button_css(''), unsafe_allow_html=True)
            analise_credito = st.button("Análise de Crédito", key="analise_credito", help="Análise de Crédito")
        
        with col3:
            st.markdown(get_button_css(''), unsafe_allow_html=True)
            comite = st.button("Comitê", key="comite", help="Comitê")
        
        with col4:
            st.markdown(get_button_css(''), unsafe_allow_html=True)
            formalizacao = st.button("Formalização", key="formalizacao", help="Formalização")
            
        with col5:
            st.markdown(get_button_css(''), unsafe_allow_html=True)
            liberacao = st.button("Liberação", key="liberacao", help="Liberação")
        
        # Organizando a segunda linha de botões centralizados
        st.markdown("<hr>", unsafe_allow_html=True)  # Adiciona um divisor após os botões do menu principal
        st.markdown("<p class='menu-title'>Apêndices:</p>", unsafe_allow_html=True)
        col6, col7 = st.columns(2)
            
        with col6:
            st.markdown(get_button_css(''), unsafe_allow_html=True)
            apendice_garantias = st.button("Apêndice 1: Garantias", key="apendice_garantias", help="Clique aqui para apêndice de garantias")
        
        with col7:
            st.markdown(get_button_css(''), unsafe_allow_html=True)    
            apendice_2 = st.button("Apêndice 2: Sites de Consultas", key="apendice_2", help="Clique aqui para apêndice 2")
        
        st.markdown("<hr>", unsafe_allow_html=True)  # Adiciona um divisor entre os apêndices
           
        # Verificar qual botão foi clicado e navegar para a respectiva subseção
        if acolhimento_proposta:
            st.subheader("Acolhimento Proposta")
            st.markdown("""
            **Colaborador(a) Responsável:**
            - Cadastro atualizado no SISBR - proponente(s), avalista(s)/fiador(es), garantidor(es)/cedente fiduciante(s), na categoria Avançado/Completo e de acordo com o Manual de Cadastro do Sicoob (principalmente contrato social e alterações contratuais, regime de casamento, endereço, renda/faturamento e patrimônio).
            - Autorização consulta SCR - proponente(s), avalista(s)/fiador(es), garantidor(es)/cedente fiduciante(s), procurador(es).
            - Cartão de assinatura atualizado no SISBR dos envolvidos para conferência das assinaturas no instrumento de crédito e demais documentos.
            - Procuração atualizada e com poderes para representar perante a Singular para assinar instrumentos de crédito, operações de repactuações, prestar aval/fiança, garantia real, entre outros.
            - Efetuado e anexado as consultas de comprovação de regularidade fiscal (FGTS, Federal, Estadual) e ambiental vigente na data da proposta, se exigidos.
            - Consultas restritivas atualizadas há menos de 30 dias junto aos órgãos de proteção ao crédito (SERASA e SCR) - proponente(s), avalista(s)/fiador(es), garantidor(es)/cedente fiduciante(s).
            - Restrições relevantes estão devidamente justificadas e/ou apresentado o comprovante de regularização pelo gerente da conta.
            - Proponente apresenta capacidade de pagamento, conforme disposto na metodologia da Singular.
            - Valor da operação, prazo, encargos financeiros, garantias, itens financiados, percentual financiado e forma de liberação dos recursos enquadrados na linha de crédito.
            - Limite de crédito vigente e deferido em alçada competente e com margem disponível no portfólio correspondente a operação de crédito pleiteada.
            - Parecer consta as informações relevantes quanto a contratação de seguro prestamista e/ou seguro do bem vinculado em garantia e registro em cartório.
            - Parecer negocial fundamentando o despacho da operação.
            - Anexado os documentos necessários para análise e formalização correta do instrumento de crédito e garantias, conforme Apêndice 1.
            
            **Nota:** Os bens de propriedade de pessoa jurídica somente serão vinculados em garantia se houver previsão expressa no contrato social ou estatuto, ou mediante avaliação jurídica específica, para que sejam adotadas as medidas necessárias à validade da constituição.
            """)

        if analise_credito:
            st.subheader("Analise de crédito")
            st.write("""
            **Colaborador(a) Responsável:**
            - Verificar se o limite de crédito se encontra vigente, deferido em alçada competente e com margem disponível no portfólio correspondente a operação de crédito pleiteada.
            - Mencionar no parecer técnico a alçada para deferimento da operação.
            - Verificar se o cadastro se encontra atualizado no SISBR - proponente(s), avalista(s)/fiador(es), garantidor(es)/cedente fiduciante(s), na categoria Avançado/Completo e de acordo com o Manual de Cadastro do Sicoob (principalmente contrato social e alterações contratuais, regime de casamento, endereço, renda/faturamento e patrimônio).
            - Verificar as consultas restritivas atualizadas há menos de 30 dias junto aos órgãos de proteção ao crédito (SERASA e SCR) - proponente(s), avalista(s)/fiador(es), garantidor(es)/cedente fiduciante(s).
            - Verificar se estão em anexo ao dossiê as consultas de comprovação de regularidade fiscal (FGTS, Federal, Estadual) e ambiental vigente na data da proposta, se exigidos.
            - Verificar se as restrições relevantes estão devidamente justificadas e/ou apresentado o comprovante de regularização pelo gerente da conta.
            - Pontuar sobre a capacidade de pagamento do proponente, conforme disposto na metodologia da Singular.
            - Em operações de Limite de Crédito Rotativo, pontuar em parecer se o limite foi utilizado de forma adequada, sem utilização contumaz.
            - Em operações de Limite Antecipação de Recebíveis, pontuar em parecer sobre o índice de liquidez e concentração de acordo com os normativos;
            - Conferir se a proposta de crédito atende aos normativos do CCS, Central e Singular.
            - Elaborar parecer técnico com informações suficientes para embasar o deferimento da operação, ao que se refere aos 5Cs do Crédito: Caráter, Condições, Capacidade, Capital, Colateral e atendendo ao disposto na Resolução CMN 1.559/1988 (alterada pela Resolução CMN 3.258/2005) -- item IX - seletividade, garantia, liquidez e diversificação de riscos.
            - Mencionar em parecer técnico as solicitações de exceções que constam no parecer negocial elaborado pelo P.A.
            - Anexado os documentos necessários para análise da proposta de crédito e das garantias, conforme Apêndice 1.
        """)
            
        if comite:
            st.subheader("Comitê")
            st.write("""
            **Colaborador(a) Responsável:**
            - Observar a alçada correta para deferimento.
            - Verificar e pontuar sobre as restrições analisadas, orienta-se que sejam ponderadas por alçada competente em parecer de deliberação.
            - Em caso de autorização para antecipar a liberação do recurso com base em prenotação cartorária em operação sujeita ao registro cartorário, dispensa de seguro prestamista e/ou seguro do bem em garantia, é necessário evidenciar tal autorização de forma clara no parecer de despacho da operação.
            - Elaborar parecer de despacho com informações suficientes para embasar o deferimento da operação, ao que se refere: Capacidade deficitária de pagamento, insuficiência de garantias, ausência de patrimônio computável do aval da operação, restritivos em nome do proponente e sócios, demais itens, incluindo posicionamento claro quanto as solicitações do P.A.
        """)

        if formalizacao:
            st.subheader("Formalização")
            st.write("""
            **Colaborador(a) Responsável:**
            - Condicionantes do despacho atendidas. Em caso de autorização para antecipar a liberação do recurso com base em prenotação cartorária em operação sujeita ao registro cartorário, dispensa de seguro prestamista e/ou seguro do bem em garantia, devidamente evidenciada no despacho da operação.
            - Caso a operação possua autorização de exceções ou desenquadramentos deliberadas através de chamado Topdesk, ele precisa estar anexado ao dossiê.
            - Documentos condicionados no parecer da análise técnica ou despacho de aprovação precisam ser anexados/arquivados no dossiê.
            - Imprimir: Instrumento de Crédito, Proposta de Adesão – Seguro Prestamista, para a coleta de assinaturas e rubricas.
            - Verificar se a combinação de assinaturas está correta no Sisbr (sócio administrador assina individualmente ou em conjunto), antes de realizar a formalização das assinaturas no instrumento de crédito.
            - Realizar a coleta e conferência das assinaturas na proposta, instrumento de crédito e demais documentos, em conformidade com cartão de assinatura atualizado no SISBR dos envolvidos, caso assinados fisicamente¹.
            - Instrumento de crédito com o carimbo “Confere instrumento e assinatura” rubricado, sob carimbo do gerente, validando as informações².
            - Instrumento de crédito devidamente formalizado (garantias, valor da operação, encargos e prazos de acordo com o despacho do comitê).
            - Bens vinculados em garantia com seguro vigente, se for o caso, conforme normativo vigente.
            - Anexado os documentos necessários para formalização correta das garantias, conforme Apêndice 1.
            
            **NOTA¹:** Para realizar a formalização das assinaturas através da utilização dos meios eletrônicos: “Assinatura Eletrônica/Digital”, faz se necessário atender as regras dispostas em normativo vigente.
            **NOTA²:** A conferência de assinaturas precisa ser evidenciada em único local no instrumento, mediante aplicação de carimbo com os dizeres “assinatura confere” (ou similar), sob visto (rubrica) e identificação do responsável pela conferência na última página que constem assinatura e rubrica, subtendendo-se que o colaborador validou também as assinaturas/rubricas apostas em páginas antecedentes.
        """)

        if liberacao:
            st.subheader("Liberação")
            st.write("""
            **Colaborador(a) Responsável:**
            - Verificar se foram cumpridas as condicionantes do despacho do comitê de crédito para a contratação da operação.
            - Verificar se o instrumento de crédito foi formalizado de acordo com o despacho do comitê de crédito (valor da operação, encargos, prazos, garantias, IOF e seguro).
            - Verificar se consta anexo ao dossiê: Instrumento de crédito registrado no(s) cartório(s), se for o caso¹.
            - Verificar se foi anexado no dossiê da operação: o instrumento de crédito rubricado em todas as páginas e assinado no fecho pelo proponente e demais partes nominadas no contrato (quando assinada fisicamente) ¹, ².
            - Verificar se foi anexado no dossiê da operação: Proposta de adesão ao seguro prestamista devidamente preenchida, assinada, rubricada e conferida, se for o caso.
            - Verificar se foi anexado os documentos necessários para formalização correta das garantias, conforme Apêndice 1.
            
            **NOTA¹:** Caso assinado via “Assinatura Eletrônica/Digital”, faz se necessário atender as regras dispostas em normativo vigente.
            
            **NOTA²:** Orientamos que os instrumentos de crédito assinados fisicamente sejam digitalizados na sequência das páginas, opção: colorido e em boa resolução. As vias originais precisam ser enviadas à empresa responsável pelo arquivamento.
        """)

        if apendice_garantias:
            st.markdown(get_button_css("Apêndice 1: Garantias"), unsafe_allow_html=True)
            st.session_state.menu = 'garantias'
            st.experimental_rerun()
        
        if apendice_2:
            st.subheader("Apêndice 2: Sites de Consultas Cadastrais e Certidões")
            
            # Tabela 1: Sites de Consulta Cadastral e Certidões
            st.write("### Sites de Consulta Cadastral e Certidões")
            st.markdown("""
            | **Descrição**                           | **Link** |
            |-----------------------------------------|----------|
            | Consulta Sintegra                       | [http://www.sintegra.gov.br/](http://www.sintegra.gov.br/) |
            | Receita Federal (CNPJ)                  | [https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) |
            | Receita Federal (CPF)                   | [https://servicos.receita.fazenda.gov.br/servicos/cpf/impressaocomprovante/consultaimpressao.asp](https://servicos.receita.fazenda.gov.br/servicos/cpf/impressaocomprovante/consultaimpressao.asp) |
            | Emissão certificado MEI                 | [https://mei.receita.economia.gov.br/certificado/consulta](https://mei.receita.economia.gov.br/certificado/consulta) |
            | Consulta de alterações contratuais (PR) | [https://www.empresafacil.pr.gov.br/certidao-online/inteiro-teor?evento%5B0%5D=655&tipo_evento=cs](https://www.empresafacil.pr.gov.br/certidao-online/inteiro-teor?evento%5B0%5D=655&tipo_evento=cs) |
            | Consulta de alterações contratuais (SP) | [https://www.jucesponline.sp.gov.br/ResultadoBusca.aspx?IDProduto=20](https://www.jucesponline.sp.gov.br/ResultadoBusca.aspx?IDProduto=20) |
            | Consulta de alterações contratuais (RS) | [https://portalservicos.jucisrs.rs.gov.br/Portal/pages/principal.jsf](https://portalservicos.jucisrs.rs.gov.br/Portal/pages/principal.jsf) |
            """)

            # Tabela 2: Sites de Consulta Jurídica
            st.write("### Sites de Consulta Jurídica")
            st.markdown("""
            | **Descrição**                  | **Link** |
            |--------------------------------|----------|
            | Jusbrasil – Nacional           | [https://www.jusbrasil.com.br/consulta-processual/](https://www.jusbrasil.com.br/consulta-processual/) |
            | Supremo Tribunal Federal       | [https://processo.stj.jus.br/processo/pesquisa/?src=1.2.1](https://processo.stj.jus.br/processo/pesquisa/?src=1.2.1) |
            | Tribunal de Justiça (PR)       | [https://consulta.tjpr.jus.br/projudi_consulta/](https://consulta.tjpr.jus.br/projudi_consulta/) |
            | Tribunal de Justiça (SP)       | [https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090](https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090) |
            | Tribunal de Justiça (RS)       | [https://www.tjrs.jus.br/novo/busca/?return=proc&client=wp_index](https://www.tjrs.jus.br/novo/busca/?return=proc&client=wp_index) |
            """)

            # Tabela 3: Certidões Necessárias nas Operações de Crédito
            st.write("### Certidões Necessárias nas Operações de Crédito")
            st.markdown("""
            | **Descrição**                  | **Link** |
            |--------------------------------|----------|
            | Simples Nacional               | [https://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes.aspx?id=21](https://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes.aspx?id=21) |
            | CND Federal (PF)               | [https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PF/Emitir](https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PF/Emitir) |
            | CND Federal (PJ)               | [https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/EmitirPGFN](https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/EmitirPGFN) |
            | CND FGTS                       | [https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf](https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf) |
            | CND Estadual (PR)              | [http://www.cdw.fazenda.pr.gov.br/cdw/emissao/certidaoAutomatica](http://www.cdw.fazenda.pr.gov.br/cdw/emissao/certidaoAutomatica) |
            | CND Estadual (SP)              | [https://www10.fazenda.sp.gov.br/CertidaoNegativaDeb/Pages/EmissaoCertidaoNegativa.aspx](https://www10.fazenda.sp.gov.br/CertidaoNegativaDeb/Pages/EmissaoCertidaoNegativa.aspx) |
            | CND Estadual (RS)              | [https://www.sefaz.rs.gov.br/sat/CertidaoSitFiscalSolic.aspx](https://www.sefaz.rs.gov.br/sat/CertidaoSitFiscalSolic.aspx) |
            | Lista Devedores - União e FGTS | [https://www.listadevedores.pgfn.gov.br/](https://www.listadevedores.pgfn.gov.br/) |
            | Certidão ITR                   | [https://coletorcafir.receita.fazenda.gov.br/coletor/consulta/consultaCafir.jsf](https://coletorcafir.receita.fazenda.gov.br/coletor/consulta/consultaCafir.jsf) |
            | Certificado CCIR               | [https://sncr.serpro.gov.br/ccir/emissao;jsessionid=ON4esvnNBI8IgEhOrY82LpdA.ccir3?windowId=ccc](https://sncr.serpro.gov.br/ccir/emissao;jsessionid=ON4esvnNBI8IgEhOrY82LpdA.ccir3?windowId=ccc) |
            """)

            # Tabela 4: Sites de Consultas Diversas
            st.write("### Sites de Consultas Diversas")
            st.markdown("""
            | **Descrição**                       | **Link** |
            |-------------------------------------|----------|
            | Consulta Nacional: CRC Contador     | [https://www3.cfc.org.br/SPW/ConsultaNacionalCFC/cfc](https://www3.cfc.org.br/SPW/ConsultaNacionalCFC/cfc) |
            | Restituição IRPF                    | [https://www.restituicao.receita.fazenda.gov.br/](https://www.restituicao.receita.fazenda.gov.br/) |
            | Reclame Aqui                        | [https://www.reclameaqui.com.br/](https://www.reclameaqui.com.br/) |
            | Whois – Dados do Site               | [https://registro.br/tecnologia/ferramentas/whois/](https://registro.br/tecnologia/ferramentas/whois/) |
            | Consumidor.gov.br                   | [https://www.consumidor.gov.br/pages/principal/?1657588660542](https://www.consumidor.gov.br/pages/principal/?1657588660542) |
            | Certidão Eleitoral                  | [https://www.tse.jus.br/servicos-eleitorais/certidoes/certidao-de-quitacao-eleitoral](https://www.tse.jus.br/servicos-eleitorais/certidoes/certidao-de-quitacao-eleitoral) |
            | Tabela Fipe                         | [https://veiculos.fipe.org.br/](https://veiculos.fipe.org.br/) |
            | Detran – Serviços (PR)              | [https://www.detran.pr.gov.br/Categoria-de-Pagina/Servicos](https://www.detran.pr.gov.br/Categoria-de-Pagina/Servicos) |
            | Detran – Serviços (SP)              | [https://www.detran.sp.gov.br/wps/portal/portaldetran/cidadao/servicos/servicosOnline](https://www.detran.sp.gov.br/wps/portal/portaldetran/cidadao/servicos/servicosOnline) |
            """)
    # Menu Apêndice de Garantias
    if st.session_state.menu == 'garantias':
        st.markdown(get_button_css(''), unsafe_allow_html=True)

        voltar = st.button("Voltar ao Menu Principal")
        if voltar:
            mostrar_menu_principal()
        
        garantia_tipo = st.selectbox(
            "Selecione o tipo de garantia",
            ("Garantia Pessoal ou Fidejussória: Aval", "Garantia Real: Imóvel", "Garantia Real: Veículos", "Garantia Real: Máquinas e Equipamentos:", "Garantia Real: Placas Fotovoltaicas", "Garantia Real: Penhor de Grãos", "Garantia Real: Penhor de Semoventes (Animais)", "Garantia Real: SGC - GARANTICOOP", "Garantia Real: Aplicação Financeira", "Garantia Real: Recebíveis: Títulos, Cheques e Duplicatas", "Garantia Real: Contrato Guarda-Chuva"),
            key='garantia_tipo'
        )
        
        apendices = {
            "Garantia Pessoal ou Fidejussória: Aval": """
                **Garantia Pessoal ou Fidejussória: Aval:**
                - Para ser considerada garantia, o coobrigado deverá dispor de recursos computáveis (bens e direitos registrados na FICAD, ou demonstrativos contábeis no caso das PJ) ou renda, em proporção, no mínimo, equivalente ao valor da dívida da qual está prestando garantia, deduzidas as próprias responsabilidades, e ou coobrigações já concedidas. A coobrigação sem a observância de recursos computáveis, ou renda compatível, é considerado aval/fiança “moral” ou “de favor” e não configura garantia, mas sim um mitigador de risco.
            """,
            
            "Garantia Real: Imóvel": """
                **a) Operações de Crédito Comercial/Rural:**
                - Matrícula atualizada, verificar ônus e averbações (validade: 30 dias).
                - Laudo de avaliação vigente emitido por empresa credenciada, conforme normativo (validade: 2 anos).
                - Apólice vigente do seguro do bem, se for o caso, ou constar no parecer negocial, a ponderação para a dispensa de contratação do seguro.
                - Termo de ciência de benfeitorias não averbadas, exceto para apartamento ou imóveis em condomínios nos quais não seja possível realizar alterações nas benfeitorias, conforme normativo vigente.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Liberação do Crédito: Para financiamento de Bens Imóveis o pagamento deverá ser feito diretamente ao vendedor do imóvel.
                - Registro no CRI – Cartório de Registro de Imóveis¹.
                    
                **Anexar as Certidões:**
                - Imóvel Rural: Efetuado e anexado as consultas de comprovação de regularidade fiscal: ITR Válido/CCIR quitado/comprovante de pagamento.
                - Imóvel Urbano: Efetuado e anexado as consultas de comprovação de regularidade fiscal: certidão negativa de débitos municipais ou equivalente.
                
                **Nota¹:** Imprimir 03 vias do instrumento de crédito: 02 vias são “não negociáveis” e 01 via é “negociável”. A via registrada em cartório é a “negociável”, a qual deve constar arquivada no dossiê da operação.
            """,
            
            "Garantia Real: Veículos": """
                **Garantia Real: Veículos:**
                
                **a) Veículos Novos:**
                - NF para veículo 0 km.
                - Apólice vigente do seguro do bem, caso contrário deve estar ponderado no parecer negocial a dispensa da contratação do seguro.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Liberação do Crédito: Para financiamento o pagamento deverá ser feito diretamente ao(s) vendedor(es), conforme nota fiscal.
                Nota: No caso de veículo adquirido de loja (garagem)/concessionaria: Constar a NF ou procuração identificando o responsável pelo recebimento dos valores.
                - Registro de gravame junto ao Detran (automático na liberação da proposta).
                
                **b) Veículos Usados:**
                - CRLV atualizado.
                - Consulta multas/ licenciamento/ IPVA/ livre de ônus.
                - Laudo de avaliação vigente emitido por empresa credenciada (validade: 1 ano) / consulta tabela FIPE/ fotos.
                - Laudo de opinião (exceções), verificar as regras de aceitação conforme normativo vigente.
                - Apólice vigente do seguro do bem, caso contrário deve estar ponderado no parecer negocial a dispensa da contratação do seguro.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Liberação do Crédito: Para financiamento o pagamento deverá ser feito diretamente ao(s) vendedor(es), conforme CRLV, quando se tratar de veículo usado.
                Nota: No caso de veículo adquirido de loja (garagem)/concessionaria: Constar a NF ou procuração identificando o responsável pelo recebimento dos valores.
                - Registro no Cetip (gravame junto ao Detran).
                - Para Financiamento: Anexar a autorização para transferência de propriedade de veículo ou recibo de compra e venda devidamente preenchido e assinado pelas partes:
                
                    **a) Assinado fisicamente:** por vendedor e comprador, e reconhecido firma em cartório.
                
                    **b) Assinado eletronicamente** (via app da CNH digital): com identificação das assinaturas do vendedor e comprador feitos pelo GOV.BR.
            """,
            
            "Garantia Real: Máquinas e Equipamentos:": """
                **Garantia Real: Máquinas e Equipamentos**
                - Matrícula onde o bem está localizado ou instalado: Penhor Rural, Industrial ou Mercantil.
                - Itens usados: Laudo de avaliação vigente (validade: 1 ano) emitido por profissional (ASTEC) ou empresa credenciada, conforme normativo.
                - Itens novos: Nota Fiscal, emitidas com data posterior a aprovação do Crédito.
                - Apólice do seguro do bem, se for o caso, ou constar no parecer negocial, a ponderação para a dispensa de contratação do seguro.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Liberação do Crédito: Para financiamento o pagamento deverá ser feito diretamente ao(s) vendedor(es).
                - Registro no CRI – Cartório de Registro de Imóveis: Penhor Rural, Industrial ou Mercantil.
                - Registro no CRTD – Cartório de Registro de Títulos e Documentos: Alienação.
            """,
            
            
            "Garantia Real: Placas Fotovoltaicas": """
                **Garantia Real: Placas Fotovoltaicas:**
                
                **a) Se as placas estiverem inclusas como garantia:**
                - Nota Fiscal, emitidas com data posterior a aprovação do Crédito.
                - Projeto técnico, em nome do emitente contendo a planilha de retorno de investimento, e assinado pelo fornecedor.
                - Apólice do seguro do bem, se for o caso, ou constar no parecer negocial, a ponderação para a dispensa de contratação do seguro.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Liberação do Crédito: Diretamente na conta corrente da empresa responsável pela execução do projeto, indicada no corpo do próprio projeto, mediante apresentação de notas fiscais.
                - Registro no CRI – Cartório de Registro de Imóveis: Penhor.
                - Registro no CRTD – Cartório de Registro de Títulos e Documentos: Alienação.
                
                **b) Se as placas NÃO estiverem inclusas como garantia:**
                - Projeto técnico, em nome do emitente contendo a planilha de retorno de investimento, e assinado pelo fornecedor;
                - Liberação do crédito: Diretamente na conta corrente do vendedor, conforme dados do projeto.
            """,
            
            
            "Garantia Real: Penhor de Grãos": """
                **Garantia Real: Penhor de Grãos:**
                **a) Para garantia de grãos já colhidos:**
                - Recibo de depósito (Certificado de depósito dos grãos armazenados);
                - Certificado de Depósito Agropecuário (CDA)/Warrant Agropecuário (WA) ou do recibo de depósito representativo do bem em garantias.
                - Relatório de posição emitido por unidade de deposito qual possui a guarda dos grãos, emitido há no máximo 30 dias, contendo assinatura e identificação do responsável da unidade.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Registro no CRI – Cartório de Registro de Imóveis: Penhor.
                **b) Para operações de crédito rural: Safra Futura**
                - Projeto técnico com previsão de receita da safra, emitido por profissional credenciado.
                - Seguro da garantia: conforme normativos.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Registro no CRI – Cartório de Registro de Imóveis: Penhor.
            """,
            
            "Garantia Real: Penhor de Semoventes (Animais)": """
                **Garantia Real: Penhor de Semoventes (Animais):**
                - Matrícula do imóvel onde os animais estão localizados.
                - Laudo de avaliação vigente emitido por empresa credenciada (validade: 1 ano), conforme normativo.
                - Ficha Sanitária dos animais (ADAPAR), ou documento equivalente.
                - Apólice do seguro do bem: Dispensado por deliberação Direx e Consad (31/08/2021).
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Liberação do Crédito: conforme normativos.
                - Registro no CRI – Cartório de Registro de Imóveis: Penhor
            """,
            
            "Garantia Real: SGC - GARANTICOOP": """
                **Garantia Real: SGC - GARANTICOOP**
                - Carta da SGC assinada (espelho da operação).
                - Deverão constar na operação, no mínimo as mesmas garantias que constam na carta, bem como os documentos obrigatórios de acordo com as garantias;
                - Cadastro da descrição da Garantia: Conforme dados da carta (inclusive o número da carta).
            """,
            
            "Garantia Real: Aplicação Financeira": """
                **Garantia Real: Aplicação Financeira**
                - Relatório da garantia (exemplo, extrato da aplicação financeira).
                - Bloqueio da aplicação automático com a inclusão na operação.
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Registro no CRTD - Cartório de Registro de Títulos e Documentos, conforme normativo.
            """, 
            
            "Garantia Real: Recebíveis: Títulos, Cheques e Duplicatas": """
                **Garantia Real: Recebíveis: Títulos, Cheques e Duplicatas:**
                - Não há documentação obrigatória;
                - Cadastro da descrição da Garantia: Conforme modelo padrão (disponível no caderno de linhas).
                - Registro no CRTD - Cartório de Registro de Títulos e Documentos, conforme normativo.
            """,
            
            "Garantia Real: Contrato Guarda-Chuva": """
            **Garantia Real: Contrato Guarda-Chuva**
            - Se o cooperado possuir limite Guarda Chuva disponível, o mesmo poderá ser incluso nas propostas.
            - Os critérios para as linhas as quais podem ser inclusos garantia do limite estão na CCI específica do produto.
            - Anexar no dossie das operações: Cópia do contrato mãe registrado em cartório e Matrícula contendo a averbação do registro da garantia em favor da Cooperativa.
            """   
        }
        
        st.markdown(apendices[garantia_tipo])

        
            
if __name__ == "__main__":
    main()