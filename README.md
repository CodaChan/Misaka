# Misaka

Misaka Voice Control Interface



## Live Example

**Usage**

Visit `http://124.222.21.77:5000/misaka?str= ` + `yourInputStr` to `GET` the result.

**Example**

```
http://124.222.21.77:5000/misaka?str=分别打开客厅和房间的台灯的电源，再打开大棚里的台灯的电源
```

The result is `客厅-台灯-电源-打开 房间-台灯-电源-打开 大棚-台灯-电源-打开`



## Deployment

**Requirement**

Tested on Ubuntu Server 20.04, refer to the requirements of [paddlepaddle](https://www.paddlepaddle.org.cn).

```
fastNLP==0.7.0
pandas==1.2.5
torch==1.10.1
tqdm==4.61.1
transformers==4.14.1
ddparser==1.0.6
```

**Step by Step**

1. Installing Dependencies.

   ```
   > pip install ddparser
   > pip install paddlepaddle
   > pip install LAC
   > pip install tqdm
   > pip install Flask
   ```

2. Execute `flask run --host=0.0.0.0` in the project root directory.

3. Visit `http://<yourServerIP or yourDomain>:5000/misaka?str= ` + `yourInputStr` to `GET` the result.'



## TODO List

- Optimized code structure
- Deployment Docker Containerized



## Thanks

[@plainfebruary (Algorithm & CodeContribution)](https://github.com/plainfebruary)

[paddlepaddle (DeepLearning)](https://www.paddlepaddle.org.cn)

[Flask (ServerDeployment)](https://flask.palletsprojects.com/en/2.0.x/)