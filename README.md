<h1>Programs for Pre-Calculus & Calculus I</h1>

## [1. TI-84 Evo & CE Programs](#1-ti-84-evo-ce)
## [2. TI-Nspire CX-II NON-CAS programs](#2-ti-nspire-cx-ii)


<a id="1-ti-84-evo-ce"></a>

## 1. TI-84 EVO & CE Programs

A collection of utility programs for TI-EVO and TI-84 Plus CE graphing calculators designed to streamline advanced algebraic and trigonometric calculations. This repository provides a toolkit to bridge the gap between floating-point decimal approximations and exact mathematical expressions, making it easier to simplify radicals, factor integers, and reverse-engineer exact values from decimals.

*Ideal For:* Math students, educators, and engineers who need quick access to exact-value outputs (rather than standard calculator decimal outputs) for homework, test-checking, or complex problem-solving.

- <h3>MINROOT</h3> 

  - Find the minimum root of a given value under a radical (the radicand).
  - Given the X integer under the radical (for Sqrt(X) just use X)
  - ex: <code>X=27 ➡️ 3*√(3)</code>

- <h3>ROOTMATC</h3> 
  
  - Find an exact root that matches a decimal value approximation.
  - <code>X=5.360475154 (represents 8*√(22)/7 )</code>
  - ex: <code>5.360475154 ➡️ 8*√22/7</code>
  
- <h3>FACTOR</h3> 

  - Find prime factors of X. 
  - ex: <code>27 ➡️ {1,3,9,27}</code>

- <h3>MOD</h3> 

  - Calc Modulus of X. Useful for finding co-terminal values.
  - ex: <code>295, 180 ➡️ 115</code> 

- <h3>PIRATIO</h3> 

  - Find the exact pi ratio of a given decimal approximation.
  - <code>X = 1.832595715 (represents 7π/12)</code>
  - ex: <code>1.832595715 ➡️ 7π/12</code> 


<h2>TI-84 Evo Links:</h2>

Online Calculator (login realityexpander)
  - [https://ti84evo.ti.com/84evo/en/main-view](https://ti84evo.ti.com/84evo/en/main-view)
  - Use "Send Files" - "send to calculator" to send a program file on computer to a the emulator calculator.
  - Use "Send Files" - "send to computer" to copy a program from the emulator calculator to your computer files.

Connect to Physical Calculator
  - [https://connectevo.ti.com/ticevo/en/main-view](https://connectevo.ti.com/ticevo/en/main-view)
  - Use "send to calculator" to send a program file to a physically connected calculator.
  - Use "send to computer" to copy a program from the physical connected calculator to your computer files.

<h3>TI-84 CE Plus Links:</h3>

Online Calculator (login realityexpander)
  - [https://ti84evo.ti.com/84evo/en/main-view](https://84plusce.ti.com/8eu/main-view)

Connect to Physical Calculator
  - Use "TI Connect CE" App
  - Use "send to calculator" to send a program file to a physically connected calculator.
  - Use "send to computer" to copy a program from the physical connected calculator to your computer files.

  - Web-based Alternative to "TI Connect CE"
    - https://ticalc.link/   

<h3>TI-84 Evo ↔ CE ↔ BASIC/Python Text File Conversion Links:</h3>

  - Convert Text File BASIC code to TI-BASIC Encoded file
    - Use TI-CONNECT CE, paste in code, save as .8xp
    - OR... Use TI-Basic Program Converter @ [https://tiplanet.org/scripts/EvoConv/](https://tiplanet.org/scripts/EvoConv/)
      - Paste in the text, save as .8xp or .8xp2

  - Convert Text File Python to TI-Python, there is no need to encode, all python programs are stored as plain text
    - Use TI Connect Evo, simply upload text file to calculator

  - TI 84 <-> TI-84 EVO TI-BASIC Program Converter (.8xp2 <-> .8xp)
    - https://tiplanet.org/scripts/EvoConv/

  - Alternative TI-BASIC Converter
    - https://www.cemetech.net/sc/
      
### Use TI-84 Plus CE Open Source emulator (TI-SmartView is discontinued as of Oct 2026)
  - Instructions on how to [install the Open Source TI-84 Emulator](Use%20TI-84%20Plus%20CE%20Open%20Source%20emulator.md)




<a id="2-ti-nspire-cx-ii"></a>

# 2. TI-Nspire CX-II NON-CAS programs

<h2>Programs for Pre-calculus on the TI-NSpire CX II (NON-CAS). Adds some functionality from CAS calculator, like converting decimals to exact values and ratios of pi, useful for confirming hand-written work on tests and quizzes, if your professor allows use of this NON-CAS calculator.</h2>

<h3>Installation</h3>

  * To Install these function libraries:
    * use TI-Nspire Student software to transfer the `XXX.tns` to the `MyLib` folder on the calculator.
    * To refresh the libraries, `[doc] -> 6. Refresh Libraries`
    * Access the functions by `[Library Key] -> 6 Custom Functions ->` pick your file & function.

<h3> <code>compint</code>: Compute Interest / Decay / Compound Interest </h3>

- <code>compint(prin,rate,period,time)</code> - compute interest given principal, rate, period, time
- <code>contcompint(prin,rate,time)</code> - compute continuously compounding interest given principle, rate, time
- <code>expdecay(init,half_life,time)</code> - compute exponential decay given Initial Amount, Half life (years), time (years)
- <code>expgrow(init,growth,time)</code> - Compute exponential growth given initial amount, growth (in a period), time (periods)

<h3><code>cvt_degs_rad</code>: Tools to convert degrees to radians and radians to degrees, find reference angles</h3>

- <code>to_degrees(x)</code> - Convert x radians to degrees, ie: (r * 180) / pi
- <code>to_radians(x)</code> - Convert x degrees to radians, ie: (d / 180) * pi
- <code>to_ref_angle(x)</code> - Convert x degrees to reference angle in Quadrant I
- <code>to_ref_rad2(n,d)</code> - Convert pi ratio radians (Numerator w/o pi, Denominator) to reference angle radians in Quadrant I
- <code>to_ref_rads(x)</code> - Convert x radians to reference angle radians in Quadrant I 

<h3><code>exacts</code>: Tools to find the exact values based on decimal approximations within an error range.</h3>

- <code>exact_pi(x)</code>
  - Improved exact_pi, convert decimal approximation of a pi ratio to an exact pi ratio, x < n*pi/1000
  - ex: `exact_pi(4.9367884556411)` ➡️ `{11., "π/", 7.}`     ie: `(11π/7)`
- `exact_pi_old(x)`
  - SLOW VERSION - Convert decimal approximation of a pi ratio to an exact pi ratio, x < 50*pi/50
  - ex: `exact_pi_old(4.9367884556411)` ➡️ `{11, "π", "/", 7}`      ie: `(11π/7)`
- `exactsq(x)`
  - Find the exact square value given a decimal value x, max ( ((20 * sqrt(100)) / (20) )
  - ex: `exactsq(10.392304845413)` ➡️ `{6., "√", 3, "/", 1 }`     ie: `(6√3)`
- `minroot(x)`
  - Given a value x under a radical, find the minimum root value. Ex: sqrt(27) -> x=27
  - ex: `minroot(27)` ➡️ `{3, "√", 3}` which means `3√3`
- `nest_rad(a,b,c)` - Given coefficients under a nested set of radicals, reduce to two separate radicals.
  - `√( (a ± √b) / c)`  ➡️  `(√x ± √y)/c` 
  - ex: `(sqrt(2 + sqrt(3)))/4, nest_rad(2,3,4)`   ➡️  `(√6 ± √2)/4`
 
<h3><code>fact</code>: Tools to finds factors of a integer, or set of polynomial coefficients.</h3>

- <code>facts(constant,lead_coeff)</code> - Gives all factors for a an equation, given the leading coefficient and ending constant, used to find roots of a complicated equation (usually above order 2), and finding an initial divisor for synthetic division.
  - <code>3*x^(3)-6*x^(2)-57*x+60,  constant (numerator "p")=60, lead_coeff (denominator "q")=3
  -  facts(60,3) ➡️
     +/- {1,2,3,4,5,6,10,12,15,20,30,60}   (factors of numerator)
     +/- {1,3}                             (factors of denominator)
     {"±",1/3,2/3,1,4/3,5/3,2,3,10/3,4,5,6,20/3,10,12,15,20,30,60}  (ascending list of factor ratios) </code>
  - One of these values will be a root of the equation 3*x^(3)-6*x^(2)-57*x+60, and a start divisor value for synthetic division.
- <code>findfact(sum,product)</code>
  - Given a simple quadratic formula, ie: x^2 + 3*x - 28, find the two factors for the two unexpanded source equations:
  - ex: <code>sum=3, product=-28, findfact(3,-20) ➡️   {−4,7} means the two unexpanded source equations are: (x-4)(x+7) for: x^2+3*x-28</code>
- <code>quadrat(a,b,c)</code>
  - Similar to polysolve, finds constants and coefficients for quadratic equations.
  - ex:`x^(2)+3*x-28 -> quadrat(1,3,−28)`   ➡️  `{−3,"±",11,"ℝ","/",2,"→",4,−7}`
    - which means: `(x-4)(x+7)`, which has real roots at `x=4, x=-7`
- `quadrat_terms(a,b,c)`
  - Similar to quadrat but gives the full terms for the factored quadratic equation (real roots only.)
  - Input: `6*x^2-8*x-8 -> quadrat_terms(6,-8,-8)`
  - Output: `{2,"(x-2)","(3x+2)"} -> 2*(3*x + 2)*(2*x - 4)`

<h3><code>law_of_cos</code>: Using the law of cosines, compute triangle values for various kinds of triangles.</h3>

- These could possibly solved better using the built-in `nsolve` command (in DEG mode): 
  - ex:`nSolve(c^2=a^2+b^2-2*a*b*cos(cd),cd)|a=3 and b=4 and c=5`   ➡️   `ad=90`
- `law_of_cos_sas(side_a, ang_c, side_b)`
  - Computes side C length. ang_c is in degrees and does not require DEG mode. 
  - ex: <code> law_of_cos_sas(3,90,4)   ➡️  5 </code>
- `law_cos_sss(side_a, side_b, side_c)`
  - Computes angle A (opposite side_a) in DEGREES.
  - ex: <code> law_of_cos_sss(3,4,5)   ➡️  36.8699° </code>
- `law_cos_ass(ang_a, side_b, side_a)`
  - Computes triangle data for 0, 1, 2 triangle cases for SSA triangles.
  - NOTE: Parameter side_b is adjacent to ang_a, side_a is opposite ang_a
  - Outputs the 1st & 2nd triangle angles, A, B, C, and length a, b, c, and if second triangle exists, the A', B', C' angles and a', b', c' sides.
  - ex: `law_cos_ass(60,15,14)`    ➡️
    `[["1△°A,B,C",60,68.1074,51.8926]`
    `["1 len a,b,c",14,15,12.72015]`
    `["2△°A',B',C'",60,111.8926,8.1074]`
    `["2 len a',b',c'",14,15,2.2798]]`
- `semi_perim(side_a,side_b,side_c)`
  - Computes semi-perimeter = (a+b+c)/2
  - ex: `semi_perimeter(3,4,5)`   ➡️  `6` 
- `tri_area(side_a,side_b,side_c)`
  - Computes area of triangle, s=semi-perimiter,  = sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
  - ex: `tri_area(3,4,5)`   ➡️  `6`
