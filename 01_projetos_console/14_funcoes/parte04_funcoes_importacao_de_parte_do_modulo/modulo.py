
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_velocidade_media(vi, vf):
    vm = vf-vi
    return vm

def calcular_tempo_medio(ti, tf):
    tm = tf-ti
    return tm

def calcular_aceleracao_media(vm, tm):
    am = vm/tm
    return am

def calcular_mru(si, v, t):
    s = si+v*t
    return s