#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_Majuscule = ''
    for lettre in mot:
        mot_Majuscule += chr(ord(lettre) - 32)
    return mot_Majuscule


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
