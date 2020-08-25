# Desafio SRE New Way

Desafio consite em 5 etapas:

1. Aplicação
2. Imagem docker da aplicação 
3. Docker  com proxy reverso
4. Monitoramento 
5. Diagrama da arquitetura e justificativas


# Aplicação + Nginx +Dockerização

Foi desenvolvida uma aplicação Vue + Flask com Crud

Que tem como finalizada o cadastro de livros Lidos e Não lidos

![enter image description here](https://i.imgur.com/G79oq22.gif)

### Como iniciar a aplicação

    $ git clone https://github.com/mgsoares7/Desafio-SRE-NewWay.git
    $ cd flask-vue-crud
    $ docker build -t web:latest .
    $ docker run -d --name flask-vue -e "PORT=8765" -p 8007:8765 web:latest


## Monitoramento Prometheus + Grafana

O Prometheus é um banco de dados de série temporal extremamente popular como banco de dados de métricas e monitoramento, o Prometheus é muito legal porque foi projetado para extrair métricas de seu aplicativo, em vez de seu aplicativo ter que enviar métricas para ele ativamente. Juntamente com o Grafana , esta pilha se transforma em uma ferramenta poderosa de rastreamento/monitoramento de métricas, que é usada em aplicativos em todo o mundo.

![enter image description here](https://i.imgur.com/CPGA2rn.png)


# Diagrama da arquitetura e justificativas

![enter image description here](https://i.imgur.com/o55NSAY.png)

O **Prometheus** é uma ferramenta de monitoramento de sistema gratuita e de código aberto que armazena todos os seus dados em um banco de dados de série temporal. Você pode ajustar facilmente a definição de suas métricas e gerar relatórios mais precisos, pois oferece uma linguagem de consulta poderosa e dados multidimensionais. Isso ajuda a representar graficamente os dados resultantes em painéis.

**Grafana** é um construtor líder de gráficos e painéis que visualiza infraestrutura de séries temporais e métricas de aplicativos. Ele permite que você crie alertas, notificações e filtros ad-hoc para seus dados.

Com isso pude montar um ambiente cloud que tenha alta disponibilidade e constante monitoramento da infra e suas aplicações

Links para verificação:

Grafana: [http://ec2-54-172-86-241.compute-1.amazonaws.com:3000/](http://ec2-54-172-86-241.compute-1.amazonaws.com:3000/) | login: admin senha: Kelvincontrataeu!o/
Prometheus: [http://ec2-54-172-86-241.compute-1.amazonaws.com:9090/](http://ec2-54-172-86-241.compute-1.amazonaws.com:9090/)
Aplicação: [http://ec2-54-172-86-241.compute-1.amazonaws.com:8007/](http://ec2-54-172-86-241.compute-1.amazonaws.com:8007/)
