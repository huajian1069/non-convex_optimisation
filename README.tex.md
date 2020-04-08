# non-convex optimisation: cma-es with gradients
#### Huajian Qiu
#### April 2020


## Introduction
A mathematical optimisation problem has the general form 

<div align="center"> 
  $minimize$ $f_0(x)$ 
  
  $subject$ $to$ $f_i(x) \leq b_i, i=1, ..., m.$
</div>

One relative simple case with nice property is called convex optimisation problem, in which the objective and constraint functions are convex, which means they satisfy the inequality

<div align="center"> 
$\[ f_i(\alpha x + \beta y) \leq \alpha f_i(x) + \beta f_i(y), i=0, ..., m. \]$
</div> 
  
With $\alpha + \beta = 1, \alpha, \beta \geq 0$. Notice, the linear programming is a special case of convex optimisation: equality replaces the more general inequality.

Nevertheless, in the context of neural network training and computer version challenges, the objective function is almost always non-linear and non-convex. Traditional techniques for general non-convex problems involve compromises. Local optimisation methods, like gradient descent, provide no information about distance to global optimum. Global optimisation method has worst-case complexity growing exponentially with problem size. As the abstraction of real CV problems, we could assume the objective function is non-convex, differentiable, and there are no constraint functions. The pursuing of better optimisation method should be based on these assumptions. 

In this project, I work on improving a global optimisation method-covariance matrix adaptation evolution strategy(CMA-ES) by exploiting **differentiablity**. Evolution strategies (ES) are stochastic, derivative-free methods for numerical optimization of non-convex continuous optimization problems. But it seems a pity that it ignores the built-in differentiablity of objective function in the context of neural network training. Therefore, the aim of this project is to integrate the information of gradient, find a better way to adjust the moving of particles in CMA-ES, get more guarantee of reaching global optimum with reasonable time cost. 

Also, based on my previous background, the methodology used in this project relies more on getting insights of optimisation method by **visualization**. Works will be more based on coding, testing, numerical experiments rather than theoretical proof. But I will combine some theoretical reasoning when necessary.  

## Progress
To simplify the development of new/improved optimisation method, we choose to begin with some common test functions of optimisation method as benchmark. [Ackley function](https://en.wikipedia.org/wiki/Ackley_function) is used in the first few weeks. Now I change to the other items on [the list](https://www.sfu.ca/~ssurjano/optimization.html).

### Week 1,2: 

Test on frist objective function: Ackley $$ f(x) = -a \exp \left\{ -b\sqrt{ \frac{1}{d} \sum_{i=1}^{d} x_i^2 }\right\} - \exp\left\{ \frac{1}{d} \sum_{i=1}^{d} \cos\left(c x_i \right) \right\} + a + e $$
$$a = 20, b = 0.2, d = 2, c = 2 \pi$$ 

- made some 2D scatter and 3D surface visualisation tools for Ackley function. 
- wrote the code of pure CMA-ES in python according to Wiki Matlab version and CMA-ES combined with line search algorithm.
- Interesting finding: experiments show CMA-ES-line-search performs much better than pure CMA-ES, especially when the initial mean of optimization variable candidates is far away from optimal.   

### Week 3,4:
- made animations about optimisation process: moving clusters of candidate parameters
- observed the round-off effect of line search, therefore add a round-off version of CMA-ES. It is not valuable by itself, but it indicates the strong relationship between local optimal and global optimal. Maybe there exist a large class of real problem where a similar relationship also exists. Then the optimisation problem will be cast to a noise-reducing problem. The key to solve this class of optimisation is to identify noise(often behaved in form of local optimal/high frequency part) and recover global information(often behaved as global optimal/low frequency part). I am still not sure how to identify the existence of this prior knowledge in objective function and how to take advantage of this inspiration. One potential way: Fourier transform.    

### week 5:
- added the visualisation of 2D normal distribution as ellipse
- refactored the code by class
- drawed the point cloud of global optimum convergence, first nice enough work to be included in final report 

### week 6:

Test on frist objective function: Bukin $$ f(x) = 100 \sqrt{|x_2 - 0.01x_1^2|} + 0.01|x_1 + 10| $$
- studyed Bukin objective function. This is interesting. Becasuse the global minima is slightly smaller than the other points on the ridge, while the points on the ridge are much smaller than the other points outside the ridge. So it is difficult to move toward global minima along the ridge, especially given the fact the ridge is a parabolic curve and shape of CMA is elliptic. The great news is that line search with small step-size still improves the original CMA a lot.  
- In Bukin case, objective function is still composed of two parts. But high frequency part is not just noise, it contains global information. Low frequenca part is delicate and need special treatment.
- Implemented one-step line search CMA-ES. It behaves more like original CMA-ES.

## Schedule
### short term
- [ ] test more objective functions
- [ ] plot grid plot of convergence


### long term
- Look forward more theoerical guidance: read books and browse slides about convex optimisation. Easter holiday is a good chance to do this.
- Also, I wonder how does anyone else tackle this problem, especially in context of neural network training. I should read some papers.
- How does CMA-ES behave compared with other heuristic method? like particle swarm optimisation(PSO), Ant colony optimisation(ACO). Distributed Intelligent System on another repository is a good example to start.


## Feedback
Open to hear any voice from you, you can write your ideas or any other comments by opening an issue. If you are interested to contribute to this project, welcome create your pull request.

I will keep on updating this repository during spring semester 2020. 

Anyway, it is assuring to share, to be open, to have a little influence in the world.

## Reference

1. CMA-ES [https://en.wikipedia.org/wiki/CMA-ES]
2. Test Objective function [https://www.sfu.ca/~ssurjano/optimization.html]
3. Convex Optimization – Boyd and Vandenberghe [https://web.stanford.edu/~boyd/cvxbook/]
4. Particle Swarm Optimisation [https://en.wikipedia.org/wiki/Particle_swarm_optimization]

   PSO appliction on robots project [https://github.com/huajian1069/Distributed-Intelligent-System.git]