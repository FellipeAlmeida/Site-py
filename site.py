import streamlit as st
import time

st.set_page_config(page_title='Fernanda', page_icon='😎')
st.title('Fernanda')

# Histórico chat
if 'mensagens' not in st.session_state:
    st.session_state.mensagens = []

# Resposta inicial do chatbot
primeira_resposta = ('Fernanda: Olá! Sou a Fernanda, um chatbot especializado em educação financeira. '
                     'Gostaria de saber sobre '
                     '**1.Impostos**, '
                     '**2.Tributos** '
                     'ou **3.Explicação educação fiscal** ')
with st.chat_message('assistant', avatar='🤓'):
    st.markdown(primeira_resposta, unsafe_allow_html=True)


# Mostrar histórico
for message in st.session_state.mensagens:
    if message['role'] == 'user':
        with st.chat_message('user', avatar='😘'):
            st.write(message['content'])
    elif message['role'] == 'assistant':
        with st.chat_message('assistant', avatar='🤓'):
            st.write(message['content'])


# Resposta usuário
if input_usuario := st.chat_input('Digite aqui...'):
    resposta_usuario = f'Você: {input_usuario}'
    input_usuario_lower = input_usuario.lower() if input_usuario else None  # Garantindo que input_usuario não seja None
    with st.chat_message('user', avatar='😘'):
        st.markdown(resposta_usuario)
    st.session_state.mensagens.append({'role': 'user', 'content': resposta_usuario})


    def fernanda_pensante():
        texto_pensante = st.empty()
        texto_pensante.text('Pensando...')
        time.sleep(1)
        texto_pensante.empty()


    def resposta_fernanda(texto):
        if any(palavra in texto for palavra in ['impostos', '1']):  # IMPOSTOS
            fernanda_pensante()
            return ('Fernanda: No Brasil, temos diversos impostos. '
                    'Você **12.gostaria** ou **13.não gostaria** de um resumo geral sobre o assunto?')

        elif any(palavra in texto for palavra in ['tributos', '2']):  # TRIBUTOS
            fernanda_pensante()
            return ('Ótimo! A tributação é um assunto amplo, '
                    '\nabrangendo diversos tipos de impostos e regras em diferentes países.'
                    '\nVocê **4.Gostaria** ou '
                    '**5.Não Gostaria** de um resumo sobre o assunto?')

        elif any(palavra in texto for palavra in ['Gostaria', '4']):
            fernanda_pensante()
            return ('Tributação é o processo pelo qual '
                    '\num governo coleta dinheiro dos cidadãos e das empresas '
                    '\npara financiar suas atividades e serviços públicos '
                    '\ncomo educação, saúde, segurança e infraestrutura. '
                    '\nIsso é feito por meio da imposição de impostos, \ntaxas e contribuições obrigatórias. '
                    '\n\nVocê gostaria de saber sobre **6.Dúvidas Tributos** ou **1.Impostos**?')

        elif any(palavra in texto for palavra in ['Não Gostaria', '5']):
            fernanda_pensante()
            return 'Ok, Gostaria de falar sobre **1.Impostos** ou **6.Dúvidas Tributos**?'

        elif any(palavra in texto for palavra in ['Dúvidas Tributos', '6']):
            fernanda_pensante()
            return ('Quais dúvidas você possui? Escolha uma das opções abaixo:'
                    '\n\n**7.Diferença entre Impostos e Tributos**\n\n'
                    'Caso sua dúvida não esteja aqui, acesse esse link:')

        elif any(palavra in texto for palavra in ['Diferença entre Impostos e Tributos', '7']):
            fernanda_pensante()
            return ('Tributo e imposto são conceitos relacionados, mas têm diferenças importantes. \n'
                    'Tributo é  uma obrigação imposta pelo Estado para arrecadar recursos. \n'
                    'É uma grande área que se subdivide em áreas menores: '
                    'taxas, impostos e contribuição de melhoria.\n'
                    'Todo tributo é compulsório e só pode ser criado ou extinto por meio de lei. \n'
                    'Por outro lado, imposto é uma categoria específica de tributo. \n'
                    'Segundo o Código Tributário Nacional, '
                    'imposto é o tributo cuja obrigação tem por fato gerador uma situação '
                    'independente de qualquer atividade estatal específica, relativa ao contribuinte. \n'
                    'Em geral, os impostos incidem sobre a renda, o patrimônio ou o consumo.\n '
                    '\n\nPortanto, todo imposto é um tributo, mas nem todo tributo é um imposto.')

        elif any(palavra in texto for palavra in ['Explicação educação fiscal', '3']):  # EDUCAÇÃO FISCAL
            fernanda_pensante()
            return ('A Educação Fiscal é um conjunto de ações educativas que visam possibilitar '
                    'a compreensão da função socioeconômica dos tributos e como eles '
                    'podem ser usados em benefício à sociedade.\n '
                    'Ela é essencial para entender o papel do Estado e como ele '
                    'pode proporcionar atividades essenciais. \n'
                    'Além disso, entendendo os conceitos fiscais, é possível saber todos os '
                    'impostos e tributos que devem ser pagos, contribuindo para que a '
                    'regularidade de empresas e pessoas físicas com a Receita fique em dia.\n\n'
                    'Gostaria de conversar sobre '
                    '**1.Impostos**, **2.Tributos** ou ir para **8.Dúvidas Educação Fiscal**?')

        elif any(palavra in texto for palavra in ['Dúvidas Educação Fiscal', '8']):
            fernanda_pensante()
            return ('Quais suas dúidas sobre a educação fiscal?\n\n'
                    '**9.Qualquer escola possui educação fiscal?**\n'
                    '**10.O que se estuda?**\n'
                    '**11.Como posso me formar na área?**')

        elif any(palavra in texto for palavra in ['Qualquer escola possui educação fiscal', '9']):
            fernanda_pensante()
            return ('Não, pois é necessário um professor formado nessa área, '
                    'instituições de ensino nas quais não possuem este profissional '
                    'não poderão ter esta disciplina.')

        elif any(palavra in texto for palavra in ['O que se estuda', '10']):
            fernanda_pensante()
            return ('Em sala de aula, os estudantes aprendem o que são os tributos e como '
                    'eles devem ser usados para se ter uma melhoria na realidade social das pessoas, '
                    'por meio de serviços públicos eficientes. '
                    '\nAlém disso, eles passam a ser motivados a observar'
                    ' como os impostos são recolhidos e aplicados na sociedade. '
                    '\nA Educação Fiscal visa estimular a conscientização da sociedade sobre a importância, '
                    'necessidade e justificativa para o pagamento de tributos.')

        elif any(palavra in texto for palavra in ['Como posso me formar na área', '11']):
            fernanda_pensante()
            return ('Existem cursos específicos sobre educação fiscal '
                    'que podem ser realizados por qualquer pessoa interessada no assunto. '
                    '\nEsses cursos podem ser oferecidos por instituições '
                    'de ensino, organizações governamentais ou não governamentais. '
                    '\n\nAqui o link de um curso sobre Educação Fiscal oferecido pelo governo: ')
        else:
            fernanda_pensante()
            return 'Desculpe, Não entendo...'

    # Resposta Fernanda
    resposta = resposta_fernanda(input_usuario_lower)
    if resposta:
        resposta_formatada = f'Fernanda: {resposta}'
        with st.chat_message('assistant', avatar='🤓'):
            st.markdown(resposta_formatada)
        st.session_state.mensagens.append({'role': 'assistant', 'content': resposta_formatada})
