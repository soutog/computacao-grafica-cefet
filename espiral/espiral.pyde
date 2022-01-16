def setup():
    background(0) # cor do fundo da tela preto
    size(1000, 1000) # altura e largura da janela
  
# função para desenhar na janela
def draw():
    
    # cor de preenchimento dos arcos nenhuma
    noFill()
      
    # cor da borda dos arcos para branco
    stroke(255, 255, 255)
    
    # numero de arcos que serao criados no loop
    n = 10
    for i in range(n):
        if i % 2 == 0: # par
            
        # função para criar um arco com centro (500,525) e largura e altura como 50px e 50px respectivamente
        # Em cada iteração alternativa, a altura e a largura os arcos aumentam em 100px. 
        # O arco começa em 90 graus que é PI/2 e termina em 270 graus (90 + 180) que é PI + meia vezes PI
            arc(500, 525, 50+i*50, 50+i*50,
                HALF_PI, HALF_PI+PI)
              
        else: # ímpar
           # função para criar um arco com centro (500,500) e largura e altura como 50px e 50px respectivamente
           # Em cada iteração alternativa, a altura e a largura os arcos aumentam em 100px. 
           # O arco começa em 270 graus que é PI + PI/2 e termina em 450 graus (90 + 360) que é 2 vezes PI + PI/2
            arc(500, 500, 50+i*50, 50+i*50, 
                HALF_PI+PI, HALF_PI + 2*PI)
