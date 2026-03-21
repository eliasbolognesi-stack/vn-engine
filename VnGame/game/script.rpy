define e = Character("Eileen") 
image bg fundo = "fundo.png"
label start:
    scene bg fundo
    with fade_black
    
    show eillen happy
    e "OI {cps=30} aparece letra por letra igual maquina{/cps}"
    call screen escolha_menu
    if _return == "legal":
        e "Obrigado!"
    else:
        e "Seu programador favorito!"
    
    e "Teste"
    
    
    
    return

screen escolha_menu:
    modal True
    frame:
        xalign 0.5 yalign 0.9  # ← MEIO HORIZONTAL + EMBAIXO
        vbox:
            spacing 20
            textbutton "Legal!" action Return("legal")
            textbutton "Quem é você?" action Return("quem")

    
