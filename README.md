# GANs-models
Данный проект представляет собой исследование и применение генеративных моделей (GANs) для создания высококачественного визуального контента. В основе проекта лежит использование мощных моделей: BigGAN, Stable Diffusion(2.1 Base/2.1/1.5), OpenJourney v4, Dreamlike Photoreal 2.0 и DALL-E 3. Каждая из них интегрируется для достижения уникальных художественных эффектов, комбинирования стилей и улучшения производительности генерации.
Проект направлен на предоставление гибкого и масштабируемого инструмента для художников, дизайнеров, исследователей и разработчиков, работающих в области генеративного дизайна и искусственного интеллекта. Подробнее с материалами можно ознакомиться на [Hugging Face](https://huggingface.co/)<img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Логотип Hugging Face" width="30px" height="30px" align="center">.

# Теория
[DALL-E 3](https://huggingface.co/ehristoforu/dalle-3-xl-v2) — это мощная генеративная модель от OpenAI, предназначенная для создания реалистичных и детализированных изображений на основе текстовых описаний. Она использует архитектуру трансформеров и сочетает в себе достижения больших языковых моделей (таких как GPT) с диффузионными моделями, которые специализированы на обработке визуальных данных.

<strong>Dreamlike Photoreal 2.0</strong> — это продвинутая диффузионная модель, предназначенная для синтеза фотореалистичных изображений на основе текстовых описаний. Модель представляет собой сочетание передовых методов в области вероятностных генеративных моделей, глубинного обучения и межмодального представления данных, что обеспечивает точное соответствие между текстовыми запросами и визуальным результатом.

<strong>OpenJourney v4</strong> — это передовая генеративная модель для создания изображений на основе текстовых описаний. Разработанная с использованием методов глубокого обучения и архитектур трансформеров, модель акцентирует внимание на адаптивности, гибкости и высоком уровне соответствия между текстом и визуальным результатом. OpenJourney v4 оптимизирована для работы в разнообразных стилях, что делает её универсальным инструментом в художественной и коммерческой графике.

<strong>BigGAN</strong> — это мощная архитектура генеративно-состязательной сети (GAN), разработанная для создания высококачественных изображений с учётом заданных классов. Модель сочетает масштабируемую архитектуру, прогрессивные методы регуляризации и стратегические модификации тренировочного процесса, что позволяет достичь выдающихся результатов в генерации изображений высокого разрешения.

<strong>Stable Diffusion</strong> — это продвинутая генеративная модель, основанная на диффузионных процессах, разработанная для создания высококачественных изображений из текстовых описаний. Эта модель сочетает передовые подходы вероятностного моделирования, глубинного обучения и латентных представлений, что позволяет эффективно генерировать визуально реалистичный контент с высокой степенью гибкости и детализации.

# Demo
<strong>Prompt №1</strong>:"A futuristic city in the clouds where houses are made of crystals and glowing plants, and the sky is painted in shades of pink and purple. In the center of the city, a massive waterfall cascades from the heavens, and winged creatures resembling dragons stroll through the streets. In the distance, floating islands with dense forests and waterfalls can be seen."
<table>
  <tr>
    <th>Model</th>
    <th>Metric (CLIP)</th>
    <th>Mechanism</th>
    <th>Img</th>
  </tr>
  <tr>
    <td rowspan="3">Stable Diffusion 2.1 Base</td>
    <td>val</td>
    <td>EulerAncestralDiscreteScheduler</td>
    <td><img src="images/prompt_1/Stable Diffusion 2.1 Base/EulerAncestralDiscreteScheduler/загруженное (1).png" alt="Model A Image" width="200"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>EulerDiscreteScheduler</td>
    <td><img src="path/to/model_b_image.png" alt="Model B Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>DDIMScheduler</td>
    <td><img src="path/to/model_c_image.png" alt="Model C Image" width="100"></td>
  </tr>
  <tr>
    <td rowspan="3">Stable Diffusion 2.1</td>
    <td>val</td>
    <td>EulerAncestralDiscreteScheduler</td>
    <td><img src="path/to/model_a_image.png" alt="Model A Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>EulerDiscreteScheduler</td>
    <td><img src="path/to/model_b_image.png" alt="Model B Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>DDIMScheduler</td>
    <td><img src="path/to/model_c_image.png" alt="Model C Image" width="100"></td>
  </tr>
  <tr>
    <td rowspan="3">Stable Diffusion 1.5</td>
    <td>val</td>
    <td>EulerAncestralDiscreteScheduler</td>
    <td><img src="path/to/model_a_image.png" alt="Model A Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>EulerDiscreteScheduler</td>
    <td><img src="path/to/model_b_image.png" alt="Model B Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>DDIMScheduler</td>
    <td><img src="path/to/model_c_image.png" alt="Model C Image" width="100"></td>
  </tr>
  <tr>
    <td rowspan="3">Dreamlike Photoreal 2.0</td>
    <td>val</td>
    <td>EulerAncestralDiscreteScheduler</td>
    <td><img src="path/to/model_a_image.png" alt="Model A Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>EulerDiscreteScheduler</td>
    <td><img src="path/to/model_b_image.png" alt="Model B Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>DDIMScheduler</td>
    <td><img src="path/to/model_c_image.png" alt="Model C Image" width="100"></td>
  </tr>
  <tr>
    <td rowspan="3">OpenJourney v4</td>
    <td>val</td>
    <td>EulerAncestralDiscreteScheduler</td>
    <td><img src="path/to/model_a_image.png" alt="Model A Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>EulerDiscreteScheduler</td>
    <td><img src="path/to/model_b_image.png" alt="Model B Image" width="100"></td>
  </tr>
  <tr>
    <td>val</td>
    <td>DDIMScheduler</td>
    <td><img src="path/to/model_c_image.png" alt="Model C Image" width="100"></td>
  </tr>
  <tr>
    <td>DALL-E 3</td>
    <td>val</td>
    <td>?</td>
    <td><img src="path/to/model_d_image.png" alt="Model D Image" width="100"></td>
  </tr>
</table>


<strong>Prompt №2</strong>:"An underwater world with bioluminescent creatures, where corals emit a soft glow and fish float in the water like birds in the sky. In the depths of the ocean, ancient ruins covered in seaweed and inhabited by giant squids can be found. At the heart of this world lies an underwater volcano, erupting bubbles and glowing particles."

<strong>Prompt №3</strong>:"An abandoned amusement park where nature has taken over, and trees wrap around carousels, and flowers grow on roller coasters. The park features old rides covered in moss and vines, as well as deserted kiosks with faded signs. At the center of the park, there is a large lake covered in lilies, where swans and ducks swim."
