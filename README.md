<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->  

<p align="center">  
  <a href="https://trbinance.com">
    <img src="https://raw.githubusercontent.com/futuristicexchanger/BinanceTrApi/main/images/logo.png" alt="Logo" width="407" height="324">
  </a>

  <h3 align="center"> Tr Binance API </h3>




  
  
<!-- TABLE OF CONTENTS -->  
## Table of Contents  
  
* [About the Project](#about-the-project)  
* [Getting Started](#getting-started)  
  * [Prerequisites](#prerequisites)  
  * [Installation](#installation)  
* [License](#license)
* [Donation](#donation)
* [Contact](#developers)  
  
  
  
  
<!-- ABOUT THE PROJECT -->  
## About The Project  
  
BinanceTR borsasında, alım-satım yapmak veya piyasa verilerini çekmek için geliştirilen kullanımı kolay ve pratik bir python kütüphanesidir.
Binance TR'nin herkese açık [API dokümanı](https://www.trbinance.com/apidocs/) referans alınarak python programlama dili ile Binance TR için özel uygulama geliştirmek isteyenler için geliştirilmiştir.

<!-- GETTING STARTED -->  
## Getting Started  
 
Kurulum yönergesi için aşağıdaki adımlar takip edilebilir.
  
### Prerequisites  
  
- python3  
- pip   
  
### Installation  

- #### Firstly Install python 3 and pip.  

#### Install From Repo

  Clone the repo  
  ```shell  
  git clone https://github.com/futuristicexchanger/BinanceTrApi
  ```  
  
  In project directory run
  ```shell
  pip install .
  ```
  or
  ```shell
  python setup.py install
  ```

#### Install via pip
  ```shell
  pip install BinanceTrApi
  ```
  
### Example usage of some methods:
```

from BinanceTrApi import BinanceTrService as service

client = service.ApiService("apikey","apisecret")

print(client.testConnectivity())

a =client.postNewLimitOrder("USDT_TRY", "SELL", 11, 8.90)

print(a)

b = client.cancelOrderById(a["data"]["orderId"])

print(b)

c= client.getAssetInformation("USDT")

print(c)

#You need to handle timestamp for now, check documentation
d= client.getAggregateTrades("BTCUSDT",client.testConnectivity()["timestamp"]-1000,client.testConnectivity()["timestamp"],20)

print(d)

e = client.getKline("BTCUSDT","4h")

print(e)
```



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- DONATION -->
## Donation
0x0986A6cB0b5b33333383A04AFc58f862e0850c02

You can send ETH and BNB on this BSC address

<!-- DEVELOPERS -->
## Developers

[Ali Çakıcı](https://www.linkedin.com/in/ali-cakici-developer/) - a.cakici2020@gtu.edu.tr

[Haldun Meriç Erbay](https://www.linkedin.com/in/haldunerbay/) - haldunerbay@gmail.com

[Yiğit Bozkurt](https://www.linkedin.com/in/ygtbzkrt/) - ygt.bozkurt@gmail.com



Project Link: [https://pypi.org/project/BinanceTrApi/](https://pypi.org/project/BinanceTrApi/)

