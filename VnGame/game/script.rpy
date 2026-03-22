define e = Character("Eileen", ctc="ctc", ctc_position="nestled") 

image bg fundo = "fundo.png" 
image ctc:
    alpha 1.0
    "seta.png"
    0.75
    alpha 0.0
    0.75
    repeat
label start:
    scene bg fundo
    with fade_black
    
    show eileen happy  # ← Corrigido: era "eillen"
    e "OI {cps=30}aparece letra por letra igual maquina{/cps}"
    call screen escolha_menu
    
    if _return == "legal":
        e "Obrigado!"
    elif _return == "quem":  # ← Corrigido: funcionará agora!
        e "{cps=30}Seu {glitch=50}programador{/glitch} favorito!{/cps}"
    
    return

screen escolha_menu:
    modal True
    frame:
        xalign 0.5 yalign 0.9
        vbox:
            spacing 20
            textbutton "Legal!" action Return("legal")
            textbutton "Quem é você?" action Return("quem")
