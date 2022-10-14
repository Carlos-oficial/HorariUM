# HorariUM

<h2>Um web scrapper para os horários da uminho em python</h2>
<hr>
<p>
    Pretende-se que o script receba um curso (e ano/perfil) e uma data e retorne um .json que contenha todas as aulas da semana respetiva à data dada como argumento.
<p>
    Para tal o script usa o módulo <code>requests</code> para obter o html da página dos horários da UM e o módulo <code>bs4</code> para extrair a informação do html obtido.
