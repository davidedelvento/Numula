# Example Numula program.
# "wasserklavier" from Six Encores by Luciano Berio

import numpy as np
from note import *
from notate import *
from nuance import *

# create the score (notes and measures)
#
def make_score():
    rh1 = n('(rh 3/16 .  ++d- 2/8 c 1/8 +c \
        3/8 -f [c (more -c more) ] \
        3/16 [ -g 3/8 (more +e- more) ] +d- 2/8 [c (more -f more) ] 1/8 ++c \
        3/16 [5/8 -f 3/8 (more -g more) ] +d- 2/8  [c (more a- more) ] 1/8 ++c \
        3/16 -f d- [c -e-] ++c \
        ')
    rh2 = n('(rh 3/16 [+c e-] [d- f] d- e- 1/4 c 1/8 c \
        3/16 [-e- +b-] +b- [--f b- +a-] [d- --b-] 1/4 [c 3/8 +g-] 1/8 -c \
        3/16 [--f +c f] +f [b- f -b-] -e- [a- d- f 1/4 a-] --d- 1/8 _ +a- \
        3/16 [c 3/8 d- g-] -b- d- +c [d- -d- 3/8 g-] [e- +e-] \
        ')
    rh3 = n('(rh 3/16 [++e- 3/8 f -b- f] [+d- +d-] [e- -f c a- f] +++f 1/4 [--f b-] 1/8 [e- -e-] \
        3/16 [-f b- +g-] [+f +f] 1/8 .  [----c +c  c +c] [-c -c] \
        3/16 . [f +e-] c [+c +c] \
       3/16 [ ---f +f f +f] +f ---c [+g- +g-] \
        ')
    rh4 = n('(rh 3/16 +++f b- [--c a-] [++f +c] \
        [--c -g-]  3/16 [b- +b-  b- +b-] [-e- b- -b-] -e- g- g- \
        [f d-] +d- 1/4 ++d- 1/8 c 3/8 b- \
        1/8 [ ---c e 1/4 a-] [f -a-] 1/4 +g 1/8 [d- +a-] [-e- +d-] \
        ')
    rh5 = n('(rh 1/32 _ 1/64 e- +d- 1/6 [e- +d-] 1/12 c 1/4 [b- -d-] +a- \
        [b- +g] 1/6 --d- 1/12 c 1/8 [+g +e- +b-] -d- \
        1/6 [d- +a- d-] 1/12 c 1/4 [b- g -c -e-] [d- +b- +f a-] \
        1/8 [g e- -a- -c] ++d- [--b- +g +d- f +d-] c [b- -e- c -f -a-] ++d- \
        ')
    rh6 = n('(rh 1/8 [(more +++d- more) e- +a- d-] c 1/4 [b- g -c a-] [g b- +f a-] \
        [g e- -a- f] [e- g +d- f] [e- c -f -d-] \
        [c e- +b- d-] 1/6 [-d- b-] [+a- c] [-d- b-] \
        1/4 [ (less -f less) c] 3/8 [+b- d- f a-] 1/8 [3/8 --f] \
        1/4 [3/4 a- c] -e- d- \
        ')
    lh1 = n('6/8 . 2/8 [--f +c (more +a- more) ] 1/8 [-d- (more +b- more) ] 2/8 [--f +e-] 1/8 [f (more +d- more) ] \
        3/8 --f [f ++a-] \
        [--f ++b-] [--f ++c] \
        [--f ++b-] 3/16 --f [++f +d-] \
        ')
    lh2 = n('3/8 [+g- --f] [+f b- ---f] [+f +e-] \
        --g- f e- \
        d- c b- \
        1/4 e- 1/8 f 1/4 [g- ++b-] 1/8 --a- 3/8 [a ++c] \
        ')
    lh3 = n(' 3/8 [b- -b-] 3/16 [c +a-] [d- -d-] 1/4 [c +g-] 1/8 [-c +c] \
        3/8 [b- f -b-] [a- +a-] \
        3/16 [g- -g-] ++b- 1/4 c 1/8 [c +c] \
        3/16 [---f +f] ++d- 3/8 [--e- -e-] \
        ')
    lh4 = n(' 3/16 [-d- -d-] [+++f +d-] ---d +++a- \
        [--e- -e-] [+++e- d-] 3/8 --d- --c \
        3/16 +c b- 1/4 a- 1/8 [++d- f] 3/16 --g [c ++e] \
        1/4 --f 1/8 [1/4 f 1/8 +d- +b-]  [c -e-] [-f +f] g \
        ')
    lh5 = n(' 1/8 [-f a- +f] [-b- +g] [a- -c -f] [+d- +b-] [c -e- -f] [+f  +d-] \
        [1/4 ---f +f 1/8 ++g +e-] [f -a-] 1/4 [a- --f -f] (less [f +f] \
        [-f +f] [-f +f] [-f +f] \
        [-f +f] [-f +f] [-f +f] less) \
        ')
    lh6 = n(' 1/4 [-f ++g b-] [d- -f -f] [f +e- +c] \
        [b- -d- -f] [f +c +a-] [g -b- f] \
        [f a- +g] 1/2 [e -g f] \
        3/4 [ (more g more) 6/4 -c -f] +f \
        ')
    ns = NoteSet()
    ns.append_ns([rh1, lh1], 'line1')
    ns.append_ns([rh2, lh2], 'line2')
    ns.append_ns([rh3, lh3], 'line3')
    ns.append_ns([rh4, lh4], 'line4')
    ns.append_ns([rh5, lh5], 'line5')
    ns.append_ns([rh6, lh6], 'line6')
    for i in range(5):
        ns.append_measure(6/8, '6/8')
    for i in range(5):
        ns.append_measure(9/8, '9/8')
    for i in range(4):
        ns.append_measure(6/8, '6/8')
    for i in range(2):
        ns.append_measure(9/8, '9/8')
    for i in range(10):
        ns.append_measure(3/4, '3/4')
    ns.done()
    return ns

#  volume

def sv1(ns):
    t = ns.vol_cur_time
    vol_seg(ns, ppp, pp, 30/8)
def sv2(ns):
    t = ns.vol_cur_time
    vol_seg(ns, pp, ppp, 9/8)
    vol_seg(ns, ppp, pp, 18/8)
    vol_seg(ns, pp, p, 9/8)
def sv3(ns):
    t = ns.vol_cur_time
    vol_seg(ns, p, mp, 27/8)
def sv4(ns):
    t = ns.vol_cur_time
    vol_seg(ns, p, ppp, 17/8)
    vol_seg(ns, ppp, pp, 15/8)
def sv5(ns):
    t = ns.vol_cur_time
    vol_seg(ns, pp, f, 24/8)
def sv6(ns):
     t = ns.vol_cur_time
     vol_seg(ns, f, ppp, 24/8)
     vol_seg(ns, ppp, ppp, 6/8)
   
def set_vol(ns):
    sv1(ns)
    sv2(ns)
    sv3(ns)
    sv4(ns)
    sv5(ns)
    sv6(ns)

    # inner voices

    vol_adjust(ns, 1.5, lambda n: 'more' in n.tags)
    vol_adjust(ns, .7, lambda n: 'less' in n.tags)

    
    # voice to top/bottom
    vol_adjust(ns, 1.2, lambda n: 'top' in n.tags and 'rh' in n.tags)
    vol_adjust(ns, .6, lambda n: 'top' not in n.tags and 'bottom' not in n.tags)
    vol_adjust(ns, .8, lambda n: 'top' not in n.tags and 'bottom' in n.tags)

    # metric accents
    #vol_adjust(ns, 1.1, lambda n: n.measure_offset==0)
    vol_adjust(ns, 0.9, lambda n: n.measure_type=='9/8' and n.measure_offset not in [0, 3/8, 6/8])
    vol_adjust(ns, 0.9, lambda n: n.measure_type=='6/8' and n.measure_offset not in [0, 3/8])
    vol_adjust(ns, 0.9, lambda n: n.measure_type=='3/4' and n.measure_offset not in [0, 1, 2])

#  timing

def st1(ns):
    tempo_seg(ns, 30/8, linear, [65,60])
def st2(ns):
    tempo_seg(ns, 9/8, linear, [65,55])
    tempo_seg(ns, 9/8, linear, [60,70])
    tempo_seg(ns, 18/8, linear, [70,80])
def st3(ns):
    tempo_seg(ns, 27/8, linear, [65,55])
def st4(ns):
    tempo_seg(ns, 24/8, linear, [55,50])
    # at this point the score has dotted quarter = quarter
    tempo_seg(ns, 6/8, linear, [30,40])
def st5(ns):
    tempo_seg(ns, 24/8, linear, [40, 50])
def st6(ns):
     tempo_seg(ns, 30/8, linear, [50, 30])
   
def set_tempo(ns):
    st1(ns)
    st2(ns)
    st3(ns)
    st4(ns)
    st5(ns)
    st6(ns)

# timing adjustment -  do this after overall tempo

# durations of the 6 lines:
t1 = 30/8
t2 = 36/8
t3 = 27/8
t4 = 30/8
t5 = 24/8
t6 = 30/8

def ta1(ns):
    t = 0
    t_adjust_notes(ns, -.2, lambda n: 'line1' in n.tags and n.pitch==41)
    roll(ns, t+6/8,  np.linspace(-.1, 0, 4))
    pause_after(ns, t+12/8, .2)
    pause_after(ns, t+30/8, .15)
def ta2(ns):
    t = t1
    pause_after(ns, t+6/8, .15)
    pause_after(ns, t+33/8, .1)
def ta3(ns):
    t = t1 + t2
    roll(ns, t+3/8,  np.linspace(-.3, .1, 7))
    pause_after(ns, t+6/8, .15)
    roll(ns, t+13/8, np.linspace(-.12, .1, 4))
    pause_after(ns, t+6/8+3/16, .15)
    roll(ns, t+21/8, np.linspace(-.12, .1, 4), pred=lambda n: 'rh' in n.tags)
def ta4(ns):
    t = t1 + t2 + t3
    roll(ns, t+6/8+3/16, np.linspace(-.12, .1, 4), pred=lambda n: 'rh' in n.tags)
    roll(ns, t+6/8+3/8,  np.linspace(-.2, .1, 3), pred=lambda n: 'rh' in n.tags)
    pause_after(ns, t+6/8+3/8, .1)
    pause_after(ns, t+15/8, .2)
def ta5(ns):
    t = t1 + t2 + t3 + t4
    roll(ns, t+6/8,  np.linspace(-.4, .1, 6))
    roll(ns, t+14/8, np.linspace(-.2, .1, 4), pred=lambda n: 'rh' in n.tags)
    roll(ns, t+16/8, np.linspace(-.2, .1, 4), pred=lambda n: 'rh' in n.tags)
    roll(ns, t+18/8, np.linspace(-.2, .1, 4), pred=lambda n: 'rh' in n.tags)
    roll(ns, t+20/8, np.linspace(-.2, .1, 5), pred=lambda n: 'rh' in n.tags)
    roll(ns, t+22/8, np.linspace(-.2, .1, 5), pred=lambda n: 'rh' in n.tags)
def ta6(ns):
    t = t1 + t2 + t3 + t4 + t5
    roll(ns, t,  np.linspace(-.3, .1, 3), pred=lambda n: 'rh' not in n.tags)
    roll(ns, t+2/8,  np.linspace(-.4, .1, 7))
    roll(ns, t+4/8,  np.linspace(-.4, .1, 7))
    roll(ns, t+6/8,  np.linspace(-.4, .1, 7))
    roll(ns, t+8/8,  np.linspace(-.4, .1, 7))
    roll(ns, t+10/8,  np.linspace(-.4, .1, 7))
    roll(ns, t+12/8,  np.linspace(-.4, .1, 7))
    roll(ns, t+14/8,  np.linspace(-.4, .1, 3), pred=lambda n: 'rh' not in n.tags)
    roll(ns, t+18/8,  [-.4, -.3, .2, -.1, -.2])
    pause_after(ns, t+14/4, 10)

def time_adjust(ns):
    ta1(ns)
    ta2(ns)
    ta3(ns)
    ta4(ns)
    ta5(ns)
    ta6(ns)
    t_random_normal(ns, .015, 2)
    
def main():
    ns = make_score()
    if True:
        set_vol(ns)
        set_tempo(ns)
        time_adjust(ns)
        ns.print()
        ns.write_midi('wasserklavier.midi')
    else:
        ns.write_midi('wasserklavier_plain.midi')

main()
