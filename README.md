# Processamento Digital de Imagens - Atividade Prática 1.2

**Aluno:** João Felipe Maciel Trindade  
**Curso:** Bacharelado em Ciência da Computação - UNEMAT  
**Semestre:** 2026/1  
**Disciplina:** Processamento Digital de Imagens  

## Descrição

Este repositório contém a implementação da **Atividade Prática 1.2 - Implementação e Governança**, desenvolvida em **Jupyter Notebook (.ipynb)**, conforme solicitado na disciplina.

O notebook foi estruturado em **20 exercícios**, com células em Markdown para organização e explicação de cada etapa. As imagens utilizadas são de **autoria própria** e ficam disponíveis no próprio repositório público do GitHub, permitindo execução correta no **Google Colab** sem depender de arquivos locais do computador.

## Estrutura do repositório

- `Atividade_Prática_1_2_Processamento_Digital_de_Imagens (1).ipynb`
- `README.md`
- `img01.jpeg`
- `img02.jpeg`
- `img03.jpeg`
- `img04.jpeg`
- `img05.jpeg`
- `img06.jpeg`
- `img07.jpeg`
- `img08.jpeg`
- `img09.jpeg`
- `img10.jpeg`

## Bibliotecas utilizadas

Para executar o notebook, utilize a instalação abaixo:

```bash
pip install opencv-python numpy matplotlib
```

## Execução no Google Colab

O notebook foi preparado para baixar as imagens diretamente do repositório público no GitHub, garantindo compatibilidade com o ambiente do Google Colab.

### Passos para executar

1. Abra o notebook no Google Colab.
2. Execute a célula de instalação das bibliotecas.
3. Execute a célula de download das imagens.
4. Em seguida, execute todas as demais células do notebook.

## Link para abrir no Google Colab

```text
https://colab.research.google.com/github/joaofelipeunemat/Processamento-de-imagem/blob/main/Atividade_Pr%C3%A1tica_1_2_Processamento_Digital_de_Imagens%20(1).ipynb
```

## Configurações necessárias

- O repositório deve estar **público**.
- O notebook deve estar salvo com o nome final atualmente presente no repositório.
- As imagens `img01.jpeg` até `img10.jpeg` devem estar enviadas na **raiz do repositório**.
- A branch utilizada no projeto é a **main**.
- Não é necessário alterar caminhos para diretórios locais, pois as imagens são carregadas diretamente do GitHub.

## Conteúdo desenvolvido

O notebook contempla os seguintes exercícios:

1. Carregamento de imagem colorida com correção BGR → RGB  
2. Exibição de atributos da imagem (`shape`, `size`, `dtype`)  
3. Salvamento da imagem em outro formato  
4. Leitura do pixel central  
5. Modificação de região com cor sólida  
6. Recorte de ROI  
7. Separação dos canais B, G e R  
8. Exibição isolada do canal verde  
9. Merge com troca de canais  
10. Conversão para tons de cinza  
11. Conversão para HSV com extração do canal de saturação  
12. Aumento de brilho com `cv2.add`  
13. Mesclagem de duas imagens com `addWeighted`  
14. Negativo fotográfico em escala de cinza  
15. Máscara binária circular  
16. Redução para 30% do tamanho original  
17. Cálculo de histograma  
18. Plot de histogramas dos canais de cor  
19. Equalização de histograma  
20. Aplicação de threshold binário simples  

## Observação final

Este trabalho foi desenvolvido de acordo com os critérios da atividade, priorizando:
- organização do notebook;
- clareza do código;
- execução correta no Google Colab;
- uso de imagens próprias;
- documentação adequada no README.
