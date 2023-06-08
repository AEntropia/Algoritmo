# Não entendi direito o enunciado, logo fiz dos dois jeitos que eu fiquei em dúvida
f = input('Digite uma frase: ').lower()
p = input('Digite a palavra para a contagem: ').lower()
q1 = f.count(p)
q2 = f.split(' ')
print(f'A frase tem {q1} palavras {p} e tem {len(q2)} palavras ao total')
