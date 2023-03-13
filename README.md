# chatSFAI
Chat bot para auxílio ao atendimento, baseado na OpenAI
O problema é que existe um limite de tokens por requisição (de 2k a 4k a depender do modelo) e existe um limite de requisições por minuto (60) na versão gratuita. Para contornar este problema, optei por não usar programação assíncrona e tive que incluir um delay de 1.5 segundos entre uma requisição e outra. Isso faz com que o modelo demore muito tempo para rodar. Outro problema foi que a versão gratuita do GPT tem um limite de requisições, que foi alcançado antes de o teste ser concluído.
Uma opção seria fazer uma assinatura para a versão paga, mas o custo seria muito elevado.
O arquivo principal é o "chatSFAI.py", que usa o arquivo "data.json" como conhecimento prévio. O jupyter notebook foi usado apenas para fazer o crawler pelas páginas da Fazenda e obter o "conhecimento prévio".
