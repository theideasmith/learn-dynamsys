## Question

I'm starting Strogatz's *Dynamical Systems and Chaos*. At the beginning he wants to develop intuition towards the concepts in dynamical systems before jumping into rigorous theory. As such, he emphases graphical analysis as opposed to analysis. 

One of the first examples he gives is the simple one dimensional system $$\dot{x} = \sin x$$ 

The following question is asked:
> For an *arbitrary* initial condition $x_0$ what is the behavior of $x(t)$ as $t \to \infty$?


First, lets turn to the graph of $\dot{x}$. 
[![enter image description here][1]][1]

> **Strogatz's Answer**

> Strogatz answers that the particle will asymptotically approach the nearest stable point on the graph; here's an example trajectory where $x_0=\frac{\pi}{2}$

[![enter image description here][2]][2]

While I intuitively understand why this would be so, being newly introduced to rigorous mathematics, I'm intellectually skeptical of myself if I think I understand an answer without first seeing some rigorous reasoning as to why it is so.

I'm hoping someone can confirm my more rigorous solution or suggest what reasoning allows him to make his argument so confidently. 

> **My answer**

> From the graph, we see that a particle dropped at any point $x_0$ will continue moving in a direction determined by $\text{sgn}(\dot{x}(x_0))$. By the graph, the magnitude of the particle's velocity decreases as it nears a stable point of $\dot{x}(x)$. Consider that after some time, the particle is sufficiently close to a point $\tilde{x}$ s.t. $\dot{x}(\tilde{x})=0$ and we can make a small angle approximation for velocity, $\dot{x}=\sin x\approx x'$, where $x'$ shifts the function such that the origin is at $\tilde{x}$. Now the derivative of velocity linearized at $\tilde{x}$ is $\dot{x}'=sgn{x'}x$ and solving this yields $x(t)=x'e^{-t}$. It can trivially be shown that $x(t)$ converges to zero as $t \to \infty$. $\square$  

This answer is very heuristic – it only describes the magnitude of distance, not direction or sign and helps understand the qualitative nature of **Fig 2.1.2**, but not rigorously. I'm looking for guidance as to make my argument more precise. Assume my formal background ends at Calc I and that I won't appreciate any advanced real analysis concepts. 

EDIT: I had originally said that the particle approaches the nearest *zero* of the graph, but I edited that to say *stable point* which is the correct limit of the system. 

[1]: https://i.stack.imgur.com/yTsa9.png
[2]: https://i.stack.imgur.com/meIZ1.png



## Answer

The answer is from [Professor Robert Israel](http://math.stackexchange.com/users/8508/robert-israel) of the University of British Columbia

Note: $f(x)=\dot{x}$ and $f(t)=x$

The point is basically this.  Consider a differential equation $\dot{x} = f(x)$, where $f$ is continuously differentiable, and initial condition $x(0) = x_0$ where $x_0$ is in an interval $(a,b)$ where $f(x) > 0$, with $f(b) = 0$.  As long as $x(t)$ stays in that interval, the differential equation says it must be increasing.  But $x(t)$ can never get to $b$, because the constant $x(t)=b$ is a solution and the Uniqueness Theorem says two solutions can never meet or cross, so $x(t)$ must be in the interval for all $t > 0$. 

> That is to say, the solution must be in some open interval $(a,b)$ by the uniqueness theorem, and $b$ is outside of that interval. Therefore, $b$ cannot be the unique solution to the system. So now we have an upper bound on the solution to the system.

The next fact is that an increasing function that is bounded above has a limit as $t \to \infty$.  Let $\lim_{t \to \infty} f(t) = L$.  Of course, $L \le b$

But it's impossible that $L < b$, because then $f(L) > 0$ and (by continuity) there would be some $\delta > 0$ and $\epsilon > 0$ such that $f(x) > \epsilon$ whenever $|x - L| < \delta$.[^2] 

> Were $L$ less than $b$ and because $f(x)$ is continuous, the limit around $L$ results in the following contradiction.  By the mean value theorem, if $f(x) < \epsilon$ when $|x-L|<\delta$ then when $|x-L|=\delta$, $f(x)=\epsilon$. Then by the mean value theorem, there must be some $x<L+\delta$ and some $x>L+\delta$ such that the derivative between them is $\epsilon$. This means that $\delta / \Delta t = \epsilon$ so $x$ will exceed $L$ at $\Delta t = \delta / \epsilon$. But this is impossible because $\lim\limits_{t\to \infty}{x(t)} = L$. Therefore, with this result that $L \geq b$ and the restraint that $L \leq b$ from before, we conclude $L=b$

But that means that when  $x$ gets is withing distance $\delta$ of $L$, it is increasing at a speed of more than $\epsilon$, so within time $\delta/\epsilon$ it will have gone past $L$, and since it must keep increasing this contradicts the assumption that the limit is $L$.  So the only possibility is that $L = b$

