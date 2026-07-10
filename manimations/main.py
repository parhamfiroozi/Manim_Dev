from manim import *
import numpy as np
import random

config.background_color = "#0a0e14"

ghaleb_farsi = TexTemplate(tex_compiler="xelatex", output_format=".xdv")
ghaleb_farsi.add_to_preamble(r"""
\usepackage{xepersian}
\settextfont{Vazirmatn}
""")

def farsi(text, **kwargs):
    return Tex(text, tex_template=ghaleb_farsi, **kwargs)

CYAN = "#66fcf1"
TEAL = "#45a29e"
GREY = "#c5c6c7"
MAGENTA = "#c724ff"
GREEN = "#39ff14"
GOLD = "#ffd369"

NAME_EN = "PARHAM FIROOZI"
NAME_FA = r"پرهام فیروزی"
DOMAIN = "simulationtheory.ir"

class BaroonMatrix(VGroup):
    NEMADHA = "01∑∆ΩλπΦ日月火水木金土アイウエオ"

    def __init__(self, tedad_sotoon=26, tedad_radif=18, **kwargs):
        super().__init__(**kwargs)
        self.nemad_list = []
        for c in range(tedad_sotoon):
            x = -7 + c * 14 / tedad_sotoon
            for r in range(tedad_radif):
                y = 4.2 - r * 8.4 / tedad_radif
                g = Text(random.choice(self.NEMADHA), font_size=18, color=GREEN)
                g.move_to([x, y, 0])
                g.set_opacity(0)
                self.nemad_list.append(g)
        self.add(*self.nemad_list)

    def cheshmak(self, sahne, run_time=2.0):
        anims = [
            g.animate.set_opacity(random.uniform(0.15, 0.9))
            for g in random.sample(self.nemad_list, k=len(self.nemad_list) // 2)
        ]
        sahne.play(LaggedStart(*anims, lag_ratio=0.01), run_time=run_time)

class SimulationTheoryDev(MovingCameraScene):
    def construct(self):
        self.shoroo_baroon()
        self.glitch_onvan()
        self.moarrefi_farsi()
        self.demo_convo()
        self.setareha_pich()
        self.payan_emza()

    def az_rast_biyay(self, mob, fasele=8, run_time=1.0, **kwargs):
        mob.shift(RIGHT * fasele)
        self.play(mob.animate.shift(LEFT * fasele), run_time=run_time, **kwargs)

    def be_chap_boro(self, mob, fasele=8, run_time=0.8, **kwargs):
        self.play(mob.animate.shift(LEFT * fasele).set_opacity(0),
                  run_time=run_time, **kwargs)

    def shoroo_baroon(self):
        baroon = BaroonMatrix()
        self.add(baroon)
        baroon.cheshmak(self, run_time=1.6)
        baroon.cheshmak(self, run_time=1.2)
        self.wait(0.3)
        self.play(FadeOut(baroon), run_time=1)

    def glitch_onvan(self):
        onvan = Text("SIMULATION THEORY", font_size=60, weight=BOLD)
        onvan.set_color_by_gradient(CYAN, MAGENTA)
        zir_onvan = Text(DOMAIN, font_size=26, color=GOLD, font="Monospace")
        zir_onvan.next_to(onvan, DOWN, buff=0.35)

        self.play(Write(onvan), run_time=2)
        self.play(FadeIn(zir_onvan, shift=UP * 0.2))

        for _ in range(6):
            offset = np.array(
                [random.uniform(-0.05, 0.05), random.uniform(-0.03, 0.03), 0]
            )
            self.play(onvan.animate.shift(offset), run_time=0.05)
            self.play(onvan.animate.shift(-offset), run_time=0.05)

        self.wait(0.5)
        self.play(onvan.animate.scale(0.5).to_edge(UP, buff=0.4), FadeOut(zir_onvan))
        self.onvan_kochak = onvan

    def moarrefi_farsi(self):
        esm_fa = farsi(NAME_FA, font_size=46, color=CYAN)
        naghsh = farsi(r"توسعه‌دهنده مانیم", font_size=34, color=GREY)
        nemone_kar = farsi(r"نمونه کار برای " + DOMAIN, font_size=30, color=GREY)
        esm_en = Text(NAME_EN, font_size=30, color=GOLD, weight=BOLD)

        naghsh.next_to(esm_fa, DOWN, buff=0.35)
        nemone_kar.next_to(naghsh, DOWN, buff=0.35)
        esm_en.next_to(nemone_kar, DOWN, buff=0.5)

        gorooh = VGroup(esm_fa, naghsh, nemone_kar, esm_en)
        gorooh.move_to(ORIGIN)

        self.az_rast_biyay(esm_fa, run_time=0.9)
        self.az_rast_biyay(naghsh, run_time=0.9)
        self.az_rast_biyay(nemone_kar, run_time=0.9)
        self.play(FadeIn(esm_en, shift=UP * 0.2))
        self.wait(1.2)

        self.play(
            LaggedStart(
                *[m.animate.shift(LEFT * 9).set_opacity(0) for m in gorooh],
                lag_ratio=0.15,
            ),
            run_time=1.4,
        )

    def demo_convo(self):
        # ----- remove the small title so heading has room -----
        self.play(FadeOut(self.onvan_kochak))

        sar_onvan = farsi(r"کانولوشن در عمل", font_size=34, color=CYAN)
        sar_onvan.to_edge(UP, buff=0.6)
        formul = MathTex(r"y(t)=\int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau",
                         font_size=38, color=GREY)
        formul.next_to(sar_onvan, DOWN, buff=0.3)

        self.az_rast_biyay(sar_onvan, run_time=1)
        self.play(FadeIn(formul, shift=UP * 0.2))

        def x_func(t):
            return np.where((t >= -1) & (t <= 1), 1.0, 0.0)

        def h_func(t):
            return np.where(t >= 0, np.exp(-1.5 * t), 0.0)

        tau_mesh = np.linspace(-6, 6, 2000)

        def y_at(t):
            return np.trapz(x_func(tau_mesh) * h_func(t - tau_mesh), tau_mesh)

        t_khorooj = np.linspace(-4, 6, 160)
        y_khorooj = np.array([y_at(t) for t in t_khorooj])

        def y_beine(t):
            return float(np.interp(t, t_khorooj, y_khorooj))

        mehvar_bala = Axes(
            x_range=[-6, 6, 2], y_range=[-0.3, 1.4, 1],
            x_length=9, y_length=2.4, tips=False,
            axis_config={"color": GREY, "font_size": 18},
        )
        mehvar_bala.next_to(formul, DOWN, buff=0.55)

        mehvar_paein = Axes(
            x_range=[-4, 6, 2], y_range=[-0.05, float(y_khorooj.max()) * 1.3, 0.5],
            x_length=9, y_length=2.2, tips=False,
            axis_config={"color": GREY, "font_size": 18},
        )
        mehvar_paein.next_to(mehvar_bala, DOWN, buff=0.6)

        bar_chasb_bala = Text("x(τ)  &  h(t-τ)", font_size=20, color=GREY)
        bar_chasb_bala.next_to(mehvar_bala, LEFT, buff=0.3).shift(UP * 0.3)
        bar_chasb_paein = Text("y(t)", font_size=20, color=GREY)
        bar_chasb_paein.next_to(mehvar_paein, LEFT, buff=0.3).shift(UP * 0.3)

        self.play(Create(mehvar_bala), Create(mehvar_paein),
                  FadeIn(bar_chasb_bala), FadeIn(bar_chasb_paein))

        monhani_x = mehvar_bala.plot(x_func, x_range=[-6, 6, 0.01], color=TEAL, use_smoothing=False)
        self.play(Create(monhani_x))

        meghdar_t = ValueTracker(t_khorooj[0])

        monhani_h = always_redraw(
            lambda: mehvar_bala.plot(
                lambda tau: h_func(meghdar_t.get_value() - tau),
                x_range=[-6, 6, 0.02], color=MAGENTA, use_smoothing=False,
            )
        )

        nahie_zarib = always_redraw(
            lambda: mehvar_bala.get_area(
                mehvar_bala.plot(
                    lambda tau: x_func(tau) * h_func(meghdar_t.get_value() - tau),
                    x_range=[-6, 6, 0.02], use_smoothing=False,
                ),
                x_range=[-6, 6],
                color=GOLD,
                opacity=0.55,
            )
        )

        neshangar = always_redraw(
            lambda: DashedLine(
                mehvar_bala.c2p(meghdar_t.get_value(), -0.3),
                mehvar_bala.c2p(meghdar_t.get_value(), 1.4),
                color=GOLD, stroke_width=1.5,
            )
        )

        monhani_khorooj = always_redraw(
            lambda: mehvar_paein.plot(
                y_beine,
                x_range=[t_khorooj[0], max(meghdar_t.get_value(), t_khorooj[0] + 1e-3), 0.02],
                color=CYAN, use_smoothing=False,
            )
        )

        noghte_khorooj = always_redraw(
            lambda: Dot(
                mehvar_paein.c2p(meghdar_t.get_value(), y_beine(meghdar_t.get_value())),
                color=GOLD, radius=0.06,
            )
        )

        self.play(FadeIn(monhani_h), FadeIn(nahie_zarib), FadeIn(neshangar),
                  FadeIn(monhani_khorooj), FadeIn(noghte_khorooj))
        self.wait(0.3)

        self.play(meghdar_t.animate.set_value(t_khorooj[-1]), run_time=8, rate_func=linear)
        self.wait(1)

        self.play(
            *[FadeOut(m) for m in (
                sar_onvan, formul, mehvar_bala, mehvar_paein, bar_chasb_bala, bar_chasb_paein,
                monhani_x, monhani_h, nahie_zarib, neshangar, monhani_khorooj, noghte_khorooj,
            )]
        )

    def setareha_pich(self):
        sath = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-5, 5, 1],
            background_line_style={"stroke_color": TEAL, "stroke_opacity": 0.25},
        )
        self.play(Create(sath), run_time=1.5)

        sath_asli = sath.copy()
        zaman = ValueTracker(0)

        def mowj_brooz(mob):
            mob.become(
                sath_asli.copy().apply_function(
                    lambda p: np.array([
                        p[0],
                        p[1] + 0.22 * np.sin(p[0] * 1.3 + zaman.get_value())
                             + 0.12 * np.cos(p[1] * 1.1 + zaman.get_value() * 0.7),
                        p[2],
                    ])
                )
            )

        sath.add_updater(mowj_brooz)
        self.play(zaman.animate.set_value(4 * PI), run_time=5, rate_func=linear)

        n_pts = 42
        zavieh = np.linspace(0, 2 * PI, n_pts, endpoint=False)
        scale = 3.6
        noghat_lemniscate = [
            np.array([
                scale * np.cos(u) / (1 + np.sin(u) ** 2),
                scale * np.cos(u) * np.sin(u) / (1 + np.sin(u) ** 2) * 1.2,
                0,
            ]) + np.array([random.uniform(-0.12, 0.12), random.uniform(-0.12, 0.12), 0])
            for u in zavieh
        ]

        setaregan = VGroup(*[
            Dot(point=p, radius=0.05, color=GOLD) for p in noghat_lemniscate
        ])

        setare_pas = VGroup(*[
            Dot(
                point=[random.uniform(-7, 7), random.uniform(-4, 4), 0],
                radius=random.uniform(0.015, 0.035),
                color=WHITE,
            ).set_opacity(random.uniform(0.2, 0.7))
            for _ in range(60)
        ])

        khatoot = VGroup(*[
            Line(noghat_lemniscate[i], noghat_lemniscate[(i + 1) % n_pts],
                 stroke_width=1, color=CYAN, stroke_opacity=0.7)
            for i in range(n_pts)
        ])

        zirnevis = farsi(r"حلقهٔ شبیه‌سازی", font_size=30, color=GOLD)
        zirnevis.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(setare_pas), run_time=1.2)
        self.play(LaggedStart(*[GrowFromCenter(st) for st in setaregan], lag_ratio=0.02),
                  run_time=2)
        self.play(Create(khatoot), run_time=2.5)
        self.az_rast_biyay(zirnevis, run_time=1)

        hamel_setare = VGroup(setaregan, khatoot)
        self.play(Rotate(hamel_setare, angle=PI / 8, run_time=3),
                  zaman.animate.set_value(8 * PI), run_time=6, rate_func=linear)

        sath.remove_updater(mowj_brooz)
        self.wait(0.5)

        self.play(
            FadeOut(sath), FadeOut(setare_pas), FadeOut(hamel_setare),
            self.gorooh_be_chap_boro(zirnevis),
        )

    def gorooh_be_chap_boro(self, mob, fasele=8):
        return mob.animate.shift(LEFT * fasele).set_opacity(0)

    def payan_emza(self):
        # small title already gone, so no need to fade again
        esm = Text(NAME_EN, font_size=50, weight=BOLD)
        esm.set_color_by_gradient(CYAN, MAGENTA)
        zir_khat = Line(
            esm.get_left() + DOWN * 0.35, esm.get_right() + DOWN * 0.35, color=CYAN
        )

        bar_chasb_fa = farsi(r"توسعه‌دهنده مانیم برای نظریهٔ شبیه‌سازی", font_size=28, color=GREY)
        bar_chasb_fa.next_to(esm, DOWN, buff=0.6)

        link = Text(DOMAIN, font_size=30, color=GOLD, font="Monospace")
        link.next_to(bar_chasb_fa, DOWN, buff=0.5)

        self.play(Write(esm))
        self.play(Create(zir_khat))
        self.az_rast_biyay(bar_chasb_fa, run_time=1)
        self.play(FadeIn(link, shift=UP * 0.2))

        self.play(self.camera.frame.animate.scale(0.85).move_to(esm), run_time=2)
        self.wait(1.2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)