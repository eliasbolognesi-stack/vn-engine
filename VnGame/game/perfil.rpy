################################################################################
## Janela de Perfil do Personagem
################################################################################

screen botao_perfil():
    frame:
        textbutton "{b}{i}Perfil{/i}{/b}":
            xalign 0.5
            yalign 0.5
            action Show("perfil_janela")
            style "perfil_button"
        xalign 0.98
        yalign 0.02
        xsize 130
        ysize 50
        background Solid("#00000080")


screen perfil_janela():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 620
        background Solid("#202020C0")
        padding (20, 20, 20, 20)

        vbox:
            spacing 12

            text "PERFIL DO PERSONAGEM" size 34 color "#FFFFFF" xalign 0.5
            text ""

            $ prota_data = persistent.prota_data
            $ g = persistent.genero
            if prota_data is not None:
                hbox:
                    spacing 40

                    vbox:
                        spacing 8
                        # Imagem do personagem na área principal (Full body)
                        if g == "mulher":
                            add "protaF.png" xysize (360, 540) xalign 0.5 yalign 0.0
                        elif g == "homem":
                            add "protaM.png" xysize (360, 540) xalign 0.5 yalign 0.0
                        else:
                            text "Imagem indisponível" size 20 color "#ffffff"

                        text "" size 10

                        text "Nome: [prota_data['nome']]" size 24
                        text "Apelido: [prota_data['apelido']]" size 24
                        text "Gênero: [prota_data['genero']]" size 24
                        text "Sexualidade: [prota_data['sexualidade']]" size 24
                        text "Ocupação: [prota_data['ocupacao']]" size 24
                        text "Espécie: [prota_data['especie']]" size 24
                        text ""
                        text "Altura: [prota_data['anatomia']['altura']]" size 24
                        text "Peso: [prota_data['anatomia']['peso']]" size 24
                        text "Raça: [prota_data['anatomia']['raca']]" size 24
                        text "Tipo Sanguíneo: [prota_data['anatomia']['tipo_sangue']]" size 24

                    vbox:
                        spacing 8
                        text "Personalidade:" size 24
                        text "- Gentileza: [prota_data['personalidade']['kind']]/100" size 22
                        text "- Inteligência: [prota_data['personalidade']['smart']]/100" size 22
                        text "- Seriedade: [prota_data['personalidade']['serious']]/100" size 22
                        text "- Humor: [prota_data['personalidade']['funny']]/100" size 22
                        text "- Saúde: [prota_data['personalidade']['healthy']]/100" size 22
                        text ""
                        text "Notas: [prota_data['notas']]" size 22

                text ""
                text "Cores principais: [', '.join(prota_data['cores_principais'])]" size 20
                text "Cores favoritas: [', '.join(prota_data['cores_favoritas'])]" size 20

            else:
                text "Nenhum personagem selecionado ainda." size 24 color "#FFCCCC"

            textbutton "Fechar" action Hide("perfil_janela") xalign 0.5 yalign 0.5:
                background Solid("#FF000080")
                padding (10, 20)
