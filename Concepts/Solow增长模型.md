---
tags: [economics, growth, dynamics, solow]
aliases:
  - Solow模型
  - Solow Growth Model
---

# Solow增长模型

> 把长期经济增长写成一个带有“积累项”和“耗散项”的动力系统。

## 1. 状态变量：资本存量

最简模型把资本 $K$ 当作核心状态变量，产出由生产函数决定：

$$
Y=F(K,L;A)
$$

若暂时把劳动 $L$ 和技术 $A$ 看作常数，则 $Y$ 可以视为 $K$ 的函数。

## 2. 资本的运动方程

若产出的固定比例 $s$ 被储蓄并转化为投资：

$$
I=sY=sF(K)
$$

资本同时会折旧：

$$
\text{折旧}=\delta K
$$

所以资本存量满足：

$$
\dot K=sF(K)-\delta K
$$

可以把它理解成一个典型动力系统：

$$
\boxed{\text{资本变化率}=\text{积累 source}-\text{折旧 decay}}
$$

其中：

- $sF(K)$：资本形成的 source term；
- $\delta K$：资本损耗的 decay term。

## 3. 稳态

稳态定义为资本存量不再变化：

$$
\dot K=0
$$

因此：

$$
sF(K^*)=\delta K^*
$$

$K^*$ 是系统的固定点。

若生产函数具有资本边际收益递减，则通常：

- $K<K^*$ 时，$sF(K)>\delta K$，所以 $\dot K>0$，资本增长；
- $K>K^*$ 时，$sF(K)<\delta K$，所以 $\dot K<0$，资本减少。

因此 $K^*$ 往往是稳定固定点。

### 图：投资、折旧与稳态

下面的图直接由生产函数

$$
F(K)=AK^\alpha
$$

生成，参数取 $A=1$、$\alpha=0.5$、$\delta=0.1$。比较两个储蓄率 $s_1=0.20$ 与 $s_2=0.35$：

![Solow steady states](../Figures/solow_steady_state.png)

可以看到提高储蓄率会把投资曲线 $sF(K)$ 向上推，从而把稳态资本存量从

$$
K_1^*=4
$$

移动到

$$
K_2^*=12.25.
$$

图由 [[../Scripts/solow_diagram.py|solow_diagram.py]] 生成。

## 4. 一个具体例子：Cobb-Douglas

令：

$$
Y=AK^\alpha,\qquad 0<\alpha<1
$$

则：

$$
\dot K=sAK^\alpha-\delta K
$$

稳态满足：

$$
sAK^{*\alpha}=\delta K^*
$$

整理得：

$$
K^*=\left(\frac{sA}{\delta}\right)^{\frac{1}{1-\alpha}}
$$

所以提高储蓄率 $s$ 会提高稳态资本存量与稳态产出。

但这并不意味着 $s$ 越高越好。

## 5. 黄金律：为什么储蓄率不是越高越好？

消费为：

$$
C=(1-s)Y
$$

若 $s=1$，那么 $C=0$。因此“最大化生产能力”并不等价于“最大化人的消费”。

真正的问题是：

$$
\max_s C^*(s)
$$

在稳态上：

$$
sF(K^*)=\delta K^*
$$

所以稳态消费可以改写为：

$$
C^*=F(K^*)-sF(K^*)=F(K^*)-\delta K^*
$$

于是原问题等价于：

$$
\boxed{\max_{K^*}\left[F(K^*)-\delta K^*\right]}
$$

这里并不是忘记了 $s$，而是利用稳态约束把 $s$ 消掉。完整因果关系是：

$$
\boxed{s\longrightarrow K^*(s)\longrightarrow C^*(K^*)}
$$

可以把它理解为：

- $s$：控制参数；
- $K$：状态变量；
- $F(K)-\delta K$：稳态下可持续消费；
- 选择 $s$ 的目的：把系统的稳定资本存量控制到消费最大的那个位置。

### 黄金律的图像

![Solow Golden Rule](../Figures/solow_golden_rule.png)

图中固定的是生产函数 $F(K)$ 与折旧函数 $\delta K$。在任意 $K$ 上，两条曲线的竖直距离就是稳态消费：

$$
C^*(K)=F(K)-\delta K
$$

这个距离存在最大值，其位置定义为黄金律资本 $K_{GR}$：

$$
K_{GR}=\arg\max_K [F(K)-\delta K]
$$

一阶条件为：

$$
\boxed{F'(K_{GR})=\delta}
$$

本例取：

$$
F(K)=\sqrt K,\qquad \delta=0.1
$$

因此：

$$
K_{GR}=25,\qquad F(K_{GR})=5,\qquad \delta K_{GR}=2.5
$$

最大稳态消费为：

$$
C^*_{GR}=2.5
$$

再从稳态条件反推出所需储蓄率：

$$
s_{GR}=\frac{\delta K_{GR}}{F(K_{GR})}=\frac{2.5}{5}=0.5
$$

所以：

$$
\boxed{s_{GR}=50\%}
$$

对于一般 Cobb-Douglas $F(K)=AK^\alpha$，可进一步得到：

$$
\boxed{s_{GR}=\alpha}
$$

图由 [[../Scripts/solow_golden_rule.py|solow_golden_rule.py]] 生成。

## 6. 黄金律的控制论直觉

在当前简化模型中，$F(K)$ 和 $\delta K$ 的形状固定，因此存在一个使

$$
F(K)-\delta K
$$

最大的资本存量。

而 $s$ 并不改变这个最大值的位置本身，它通过资本动力学

$$
\dot K=sF(K)-\delta K
$$

控制系统最终稳定在哪个 $K^*$。

所以黄金律可以看成一个控制问题：

> 调整控制参数 $s$，使动力系统的稳定点 $K^*(s)$ 恰好落在使稳态消费最大化的 $K_{GR}$。

## 7. 为什么只靠资本积累，长期增长会停下来？

继续使用 Cobb-Douglas：

$$
F(K)=AK^\alpha,\qquad 0<\alpha<1
$$

资本运动方程是：

$$
\dot K=sAK^\alpha-\delta K
$$

两边除以 $K$，得到资本增长率：

$$
\boxed{g_K\equiv\frac{\dot K}{K}=sAK^{\alpha-1}-\delta}
$$

因为：

$$
\alpha-1<0
$$

所以随着 $K$ 增大：

$$
K^{\alpha-1}\downarrow
$$

从而：

$$
g_K\downarrow
$$

最终到达稳态时：

$$
sAK^{*\alpha}=\delta K^*
$$

等价于：

$$
sAK^{*\alpha-1}=\delta
$$

因此：

$$
\boxed{g_K=0}
$$

这意味着：**资本积累自己会因为边际收益递减而把资本增长率逐渐压到零。**

### 7.1 数值轨迹：资本收敛到稳态

下图数值积分：

$$
\dot K=sAK^\alpha-\delta K
$$

取：

$$
A=1,\quad \alpha=0.5,\quad s=0.2,\quad \delta=0.1,\quad K_0=0.25
$$

理论稳态为：

$$
K^*=4
$$

![Solow convergence level](../Figures/solow_convergence_levels.png)

可以看到：初始资本较低时增长较快；越接近 $K^*$，变化越慢；最终轨迹渐近稳态。

### 7.2 增长率本身趋近于零

![Solow convergence growth rate](../Figures/solow_convergence_growth.png)

资本增长率满足：

$$
g_K=sAK^{\alpha-1}-\delta
$$

随着 $K$ 上升，第一项不断下降，所以：

$$
\boxed{g_K(t)\to0}
$$

如果技术 $A$ 固定，而产出是：

$$
Y=AK^\alpha
$$

那么当：

$$
K\to K^*
$$

也有：

$$
Y\to Y^*
$$

因此长期：

$$
\boxed{g_Y\to0}
$$

### 7.3 Level effect 与 growth effect

提高储蓄率 $s$ 会提高：

$$
K^*,\qquad Y^*
$$

所以会产生更高的长期**水平（level）**。

但如果 $A$ 不增长，新的稳态仍然满足：

$$
g_K=0,\qquad g_Y=0
$$

因此：

> 提高储蓄率可以把系统推向一个更高的稳态，但不能单靠资本积累创造永久的正增长率。

从动力系统视角，这更像是**移动固定点的位置**，而不是让状态变量永久向上漂移。

这自然引出下一步：如果现实中的人均产出能够长期持续增长，那么必须有某个量不断改变生产系统本身，例如技术/生产率 $A(t)$。

图由 [[../Scripts/solow_convergence.py|solow_convergence.py]] 数值生成。

## 8. 一个重要限制：黄金律只关心最终稳态

黄金律只比较不同稳态下的长期消费，并没有评价从当前状态 $K_0$ 到新稳态之间的过渡过程。

如果今天为了达到更高的未来资本而突然提高储蓄率，当前消费会先下降。于是进一步的问题变成：

> 今天少消费一点换未来多消费一点，到底值不值？

这就需要对整条消费路径赋予价值，而不是只看最终稳态。这将自然进入 [[Ramsey模型]]。

## 9. 与此前知识的连接

- [[投资]] 是资本存量的流入量。
- [[折旧]] 是资本存量的流出量。
- [[边际收益递减]] 使投资曲线最终追不上线性的折旧曲线，从而形成稳态。
- [[跨期选择]] 解释为什么提高储蓄会牺牲当前消费。
- [[存量与流量]] 提供了理解 $K$ 与 $I$ 的数学语言。
- 技术进步 $A(t)$ 将成为解释持续长期增长的下一层机制。

[[经济学学习地图|← 返回学习地图]]
