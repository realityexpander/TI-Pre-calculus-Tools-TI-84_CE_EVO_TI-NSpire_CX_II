<h1>Programs for Pre-Calculus & Calculus I</h1>

## [1. TI-84 Evo & CE Programs](#1-ti-84-evo-ce)
## [2. TI-Nspire CX-II NON-CAS programs](#2-ti-nspire-cx-ii)


<a id="1-ti-84-evo-ce"></a>

## 1. TI-84 EVO & CE Programs

A collection of utility programs for TI-EVO and TI-84 Plus CE graphing calculators designed to streamline advanced algebraic and trigonometric calculations. This repository provides a toolkit to bridge the gap between floating-point decimal approximations and exact mathematical expressions, making it easier to simplify radicals, factor integers, and reverse-engineer exact values from decimals.

*Ideal For:* Math students, educators, and engineers who need quick access to exact-value outputs (rather than standard calculator decimal outputs) for homework, test-checking, or complex problem-solving.

- <h3>MINROOT</h3> 

  - Find the minimum root of a given value under a radical.
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
  - You will need to copy the ROM from your calculator to your computer to run the emulator on your computer.
    - There are 1 or 2 programs you will need to download to the calculator to make this work.
  1. Download the "CE-EMU" Application (A free TI-84 Emulator program for Mac/Win/Linux)
     - [https://github.com/CE-Programming/CEmu](https://github.com/CE-Programming/CEmu/releases)
     - Install the program on your computer using the correct installer (Mac, Win, Linux)
  3. Launch "CE-EMU" and run the "ROM setup wizard..."
     - (it should pop up automatically upon first launch of app.)
     - click the "Save Program" button and name the file "ROMDUMP", save it to your computer. This will be transferred to your physical calculator to extract the the ROM files from your physical calculator.
     
      <img width="238" alt="Screenshot 2026-08-01 at 12 30 40 PM" src="https://github.com/user-attachments/assets/00dcc709-b3b9-426d-9c7e-e2a73d8610d1" />
    
  4. Transfer the "ROMDUMP.8xp" to your physical calculator using "TI-Connect CE".
  5. Check your OS version number on your physical calculator.
     -   [2nd]  →  [mem/+]  →  [1.About] [ENTER] 
  6. If your physical calculator has OS 5.3 to 5.8.4, you will need to download and transfer the "Artifice" jailbreak program to physical calculator using TI-Connect CE. This program allows your calculator to run old assembly programs on your TI-84 Plus CE physical calculator.

     - https://yvantt.github.io/arTIfiCE/

     <img width="212" alt="image" src="https://github.com/user-attachments/assets/c9838fb4-80b1-439f-9c52-9552014e2524" />

  7. Run the TI-BASIC "ROMDUMP" program to extract the ROM image from the physical calculator.

     - If OS>=5.3,
       - You will need to run the "Artifice" jailbreak program for this more recent OS.
       - This program lets you run old Assembly programs, like "ROMDUMP".
       - The Artifice program is called "A".
       - 7a.

         [prgm] → [TI-Basic] → A → prgmA → ROMDUMP [ENTER] 

     - If OS<5.3,
       - On your physical calculator, Run the "ROMDUMP" program
       - 7b.

         [prgm] → [TI-Basic] → ROMDUMP [ENTER] 
  
      - This will save a copy of the ROM into the calculator main memory as a series of files (ROMData segments of 64k binary ROM info.)
  8. Using "TI-Connect CE", copy all the "ROMData#" (Where # is a letter from A to Z) segments from the physical calculator to your computer.
  
       - <img width="398" alt="image" src="https://github.com/user-attachments/assets/33d1f51e-70c6-48b4-beee-bcc25c01c067" />
  9. Drag and Drop all these "ROMData#" files from your computer to the "Drop ROM Segments Here" target.

       - <img width="238" alt="image" src="https://github.com/user-attachments/assets/8de3576e-dcbd-49a4-ab07-7cc7484e3426" />
  11. The "CE-EMU" program will then boot up the calculator with the ROMDUMP data and show the calculator startup screen.
  12. Transfer programs
     -  You may now drag and drop files to the "CE-EMU" calculator window to load, run and edit programs.
      
        <img width="452" alt="image" src="https://github.com/user-attachments/assets/6aab6d69-8a84-48f2-8f79-824ff8a5c63d" />

        <img width="452" alt="image" src="https://github.com/user-attachments/assets/d7cce519-f066-415f-82ce-a9b4b6afa29a" />




<a id="2-ti-nspire-cx-ii"></a>

# 2. TI-Nspire CX-II NON-CAS programs

<h2>Programs for Pre-calculus on the TI-NSpire CX II (NON-CAS). Adds some functionality from CAS calculator, like converting decimals to exact values and ratios of pi, useful for confirming hand-written work on tests and quizzes, if your professor allows use of this NON-CAS calculator.</h2>
<h3><i>compint</i>: Compute Interest / Decay / Compound Interest </h3>

- <code>compint(prin,rate,period,time)</code> - compute interest given principal, rate, period, time
- <code>contcompint(prin,rate,time)</code> - compute continuously compounding interest given principle, rate, time
- <code>expdecay(init,half_life,time)</code> - compute exponential decay given Initial Amount, Half life (years), time (years)
- <code>expgrow(init,growth,time)</code> - Compute exponential growth given initial amount, growth (in a period), time (periods)

<h3><i>cvt_degs_rad</i>: Convert degrees to radians and radians to degrees, reference angles</h3>

- <code>to_degrees(x)</code> - Convert x radians to degrees, ie: (r * 180) / pi
- <code>to_radians(x)</code> - Convert x degrees to radians, ie: (d / 180) * pi
- <code>to_ref_angle(x)</code> - Convert x degrees to reference angle in Quadrant I
- <code>to_ref_rad2(n,d)</code> - Convert pi ratio radians (Numerator w/o pi, Denominator) to reference angle radians in Quadrant I
- <code>to_ref_rads(x)</code> - Convert x radians to reference angle radians in Quadrant I 

<h3><i>exacts</i>: Find the exact values based on decimal approximations within an error range.</h3>

- <code>exact_pi(x)</code>
  - Improved exact_pi, convert decimal approximation of a pi ratio to an exact pi ratio, x < n*pi/1000
  - <code>ex: exact_pi(4.9367884556411) ➡️ {11., "π/", 7.}     ie: (11π/7) </code>
- <code>exact_pi_old(x)</code>
  - SLOW VERSION - Convert decimal approximation of a pi ratio to an exact pi ratio, x < 50*pi/50
  - <code>ex: exact_pi(4.9367884556411) ➡️ {11, "π", "/", 7}      ie: (11π/7) </co
- <code>exactsq(x)</code>
  - Find the exact square value given a decimal value x, max ( ((20 * sqrt(100)) / (20) )
  - <code>ex: exactsq(10.392304845413) ➡️ {6., "√", 3, "/", 1 }     ie: (6√3)</code>
- <code>minroot(x)</code>
  - Given a value x under a radical, find the minimum root value. Ex: sqrt(27) -> x=27
  - ex: <code> minroot(27) ➡️ {3, "√", 3} which means 3√3</code>
- <code>nest_rad(a,b,c)</code> - Given coefficients under a nested set of radicals, reduce to two separate radicals.
  - √( (a ± √b) / c)  ➡️  (√x ± √y)/c 
  - ex: (sqrt(2 + sqrt(3)))/4, nest_rad(2,3,4)   ➡️  (√6 ± √2)/4
 
<h3><i>fact</i>: Tools to finds factors of a integer, or set of polynomial coefficients.</h3>

- <code>facts(constant,lead_coeff)</code> - Gives all factors for a an equation, given the leading coefficient and ending constant, used to find roots of a complicated equation (usually above order 2), and finding an initial divisor for synthetic division.
  - <code>3*x^(3)-6*x^(2)-57*x+60,  constant (num)=60, lead_coeff (denom)=3
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

<h3><i>law_of_cos</i>: Using the law of cosines, compute triangle values for various kinds of triangles.</h3>

- These could possibly solved better using the nsolve command (in DEG mode): 
  - ex:<code>nSolve(c^2=a^2+b^2-2*a*b*cos(cd),cd)|a=3 and b=4 and c=5   ➡️   ad=90</code>
- <code>law_of_cos_sas(side_a, ang_c, side_b)</code>
  - Computes side C length. ang_c is in degrees and does not require DEG mode. 
  - ex: <code> law_of_cos_sas(3,90,4)   ➡️  5 </code>
- <code>law_cos_sss(side_a, side_b, side_c)</code>
  - Computes angle A (opposite side_a) in DEGREES.
  - ex: <code> law_of_cos_sss(3,4,5)   ➡️  36.8699° </code>
- <code>law_cos_ass(ang_a, side_b, side_a)</code>
  - Computes triangle data for 0, 1, 2 triangle cases for SSA triangles.
  - NOTE: Parameter side_b is adjacent to ang_a, side_a is opposite ang_a
  - Outputs the 1st & 2nd triangle angles, A, B, C, and length a, b, c, and if second triangle exists, the A', B', C' angles and a', b', c' sides.
  - ex: <code> law_of_cos\law_cos_ass(60,15,14)    ➡️
    [["1△°A,B,C",60,68.1074,51.8926]
    ["1 len a,b,c",14,15,12.72015]
    ["2△°A',B',C'",60,111.8926,8.1074]
    ["2 len a',b',c'",14,15,2.2798]] </code>
- semi_perim(side_a,side_b,side_c)</code>
  - Computes semi-perimeter =(a+b+c)/2
  - ex: <<code> semi_perimeter(3,4,5)   ➡️  6 </code>
- tri_area(side_a,side_b,side_c)</code>
  - Computes area of triangle, s=semi-perimiter,  =sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
  - ex: <code> tri_area(3,4,5)   ➡️  6 </code>
