What is Generative AI ?
---

- It is combinations of `Generative` and `AI`.

- It is beyond one step to AI and it will generate some new content using AI for you.

- For Instance, 
1. Ask for wirte a mail for Refund,
2. Text to Image, Photo, Video,
3. Generate DevOps related code like python code, github actions code.

- Generative AI is a type of AI that can `create new contents` such as `audio`, `images`, `text`, `code`, `video`.

What is pre-requisite should required to explore Generative AI ?
---

1. `Artificial Intelligence`
2. `Machine Learning`
3. `Deep Learning`

1. Artificail Intelligence - Is a development of machines that perform tasks that requires human intelligence.

- For instance, You can create AI System that can diagnosis deases from x-ray or they can predict, Or they can detect Credit Cards Frauds.

But, How machines can be intelligence as humans ?

- Here, `Machine Learning` comes into pictures.

2. Machine Learning 

- You are trying to make machine to learn something.
- Train the machine in a such a way that they can make predictions, decisions all by learning itself and work on that tasks without human involvement.

  1. Lots of training data
  - To trains machines, you will requires a lot of data to learn the machines

  2. computational power
  - we will requires a computations powers to store data, process data etc

  3. Algorithms
  - This is a way to learn the model , machines to make decisions, identify patterns, process the data.


3. Deep Learning

- Deep learning is a subset of machine learning that focuses on teaching computers to learn and make decisions by processing data through `neural networks` to gives you much much highly accurate and better results 

![alt text](learnm.png)

- For Instance, I asked to ChatGPT what is LLM ?
- It gives me ans with Bullet Points and generate new content by using AI and LLM behind the scenes.

- While i ask How they build ?
- It will not ask you that `What did you ask for How they build means what ?`
- Bcz, Generative AI, Deep Learning model has remember your questions and from their it will learns from histroy, process it, generate new contents.

What is LLM ?
---

- Large Language Models (LLMs) are AI Models to `Designed for understanding and generating human-like text. But, **TEXT** Only, Not for Videos, Images like Generative AI.

- LLM means they can generate text, process text, they can understand text, they know about words, grammers, sentences, contexts all of this will create accuracy.

**Key Points on LLM:**

- `Pre-Training` - Trained on huge corpusof data to get accuracy. Ex. ChatGPT 3 was trained with 500 GB of data.

- `Size and Scale` 
  - LLM Use Massive Neural Networks that are called `Transformars` which uses lot of parameters.

  - Highest number or parameters the better your models in training, understanding and generate capability

  - Ex. ChatGPT 3 was trained on 175 B Parameters.

- `Fine-Tuning` - More **Targeted** training for specific tasks.

**Use case of LLM**

  - Content generations - Marketing, advertising etc
  - Chatbots and Virtual assistant - Customer supports by chatbot of company

  - Language translations

  - Text summarizations


Prompt Engineering
---

- You are asking to 

**Alexa** - How's the weather ?
**Siri** - Will it rain today ?
**Google** - Red velvet cack recipe

- Whenever you are asking questions, Giving Instructions and Input to an AI System to get desired response that is a **Prompt**.

Embeddings
---

Machines DO NOT understand TEXT
They only understand numbers

Embeddings are `numerical representations of text`.

- They understand the object, relations between words, who is first and after.

- This capability will give to LLM by Embeddings.

- Embedding will create paragraph, bullet points etc.

- Embeddings used numbers only, They will get Input from users, like

  - `I eat ice cream`

- Now, each word will chuncking like devided into small parts like `I`, `eat`, `ice`, `cream`.

- Now, it will go to nural networks called transformers , processed it, Embeddings will convert into numbers, passing through numbers of tranformers layers and after that user will get final output.



Fine-Tunings
---

- To trains the AI Model to work on specific tasks to get better results.

- It will not creating intelligence from scratch

- AI Model has been already trained on foundation level then we will train model on specific tasks.

## Fine Tune Types

### 1. Self-Supervised

- The model learns from unlabeled data by predicting parts of the data itself.

```bash
"The sky is ____"
```

- Model learns to predict blue.
- No human labels required.

### 2. Supervised

- You give Input with `lables`.
- `lable` is required

```txt
User: Write refund email
Assistant: Dear customer...
```

### 3. Reinforcement

- Instead of fixed answers, the model learns from **`Feedback Signals`**.





