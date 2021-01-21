from collections import Counter

text1 = """Python é uma linguagem de programação poderosa e fácil de aprender. 
        Ela possui uma sintaxe simples e por isso é muito utilizada pelas mais diversas áreas da computação 
        para escrever diversos programas. 
        Com Python é possível trabalhar com aplicações web e desktop, apps para dispositivos móveis, 
        scripts para análises de dados e outras possibilidades.
        Essa linguagem possui uma sintaxe concisa e muitos recursos nativos, permitindo ao programador criar mais
        funcionalidades, escrevendo menos código.
        """

text2 = """O Docker é um projeto de software livre para automatizar a publicação de sistemas através de contêineres.
        Os contêineres são autossuficientes, portáteis e podem ser executados na nuvem ou localmente.
        Os contêineres do Docker podem ser executados em qualquer lugar, por exemplo:
        localmente no datacenter do cliente, em um provedor de serviços externo ou na nuvem,
        através de serviços como Azure, AWS, ou Google Cloud.
        O uso do Docker pode auxiliar muito no processo de distribuição de aplicações,
        dispensando todo o processo de configuração de ambiente, o que agiliza a implantação.
        """


def analyse_total_appearance_characters(text):

    total_count = Counter(text.lower())
    total_characters = sum(total_count.values())
    text_dict = []
    for letter, frequency in total_count.items():
        text_dict.append((letter, frequency / total_characters))

    for key, value in Counter(dict(text_dict)).most_common(10):

        print(f'Letter: "{key}", appeared {round(value * 100, 2)}%')


analyse_total_appearance_characters(text1)
print("###########")
analyse_total_appearance_characters(text2)
