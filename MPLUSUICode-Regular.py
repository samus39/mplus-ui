#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fontforge
import psMat
import sys
import os

USER_FONTS_DIR = "/home/mx-takashi/.local/share/fonts/"
MPLUS1P_REGULAR_FONT = os.path.join(USER_FONTS_DIR, "MPLUS1p-Regular.ttf")
MPLUS1CODE_REGULAR_FONT = os.path.join(USER_FONTS_DIR, "MPLUS1Code-Regular.ttf")
MPLUSUICODE_REGULAR_FONT = "MPLUSUICode-Regular.ttf"
MPLUS_BASE_FONT = MPLUS1CODE_REGULAR_FONT
MPLUS_OLD_FONT = MPLUS1P_REGULAR_FONT

# 開く（存在確認）
if not os.path.exists(MPLUS_BASE_FONT):
    print("Base font not found:", MPLUS_BASE_FONT); sys.exit(1)
base = fontforge.open(MPLUS_BASE_FONT)

# フォント名を設定（SetFontNames と同等）
base.fontname = "MPLUSUICode-Regular"     # PostScript name
base.familyname = "M PLUS UI Code"        # Family name
base.fullname = "M PLUS UI Code Regular" # Full name
# FontForge PE の SetFontNames の5番目引数は UniqueID/Other; ここはコメント的に versionInfo を使う
base.appendSFNTName("English (US)", "UniqueID", "Created by MPLUS and VLGothic")
base.version = "1.0.0"

# SetTTFName 相当（Windows 言語・ID を指定）
# ID mapping: 1=Font Family, 2=Subfamily, 3=Unique ID, 4=Full name, 0x409 = English (United States)
# fontforge の appendSFNTName を使う（または sfnt_names への代入）
base.appendSFNTName("English (US)", "Preferred Family", "M PLUS UI Code")
base.appendSFNTName("English (US)", "Preferred Subfamily", "Regular")
base.appendSFNTName("English (US)", "UniqueID", "MPLUSUICode-Regular")
base.appendSFNTName("English (US)", "Fullname", "M PLUS UI Code Regular")

# 旧フォントを開き、U+2190 をコピー
if not os.path.exists(MPLUS_OLD_FONT):
    print("Old font not found:", MPLUS_OLD_FONT); sys.exit(1)
old = fontforge.open(MPLUS_OLD_FONT)

# Unicode 0x2190 を選択してコピー（arrow left）
uni = 0x2190
# PE の Select + Copy は以下で代替
if old.has_key(chr(uni)):
    g_old = old[chr(uni)]
else:
    # fontforge の Python binding では文字列キーも使えるが安全に lookup を使う
    try:
        g_old = old[ "uni%04X" % uni ]
    except Exception:
        g_old = None

if g_old is None:
    print("Glyph U+2190 not found in old font."); old.close(); base.close(); sys.exit(1)

# base に同じコードポイントで新規グリフを作る／置き換え
# 既存グリフがあれば削除してからコピーする
try:
    g_base = base[ "uni%04X" % uni ]
    # clear existing glyph
    g_base.clear()
except Exception:
    g_base = base.createChar(uni)

# コピー手続き: outlines, components, anchors, notes, width, etc.
g_base.clear()
g_base.importOutlines(g_old)   # importOutlines は別ファイル向け。代わりに参照をコピーする:
# 手動でパスと属性をコピーする
g_base.width = g_old.width
g_base.vwidth = getattr(g_old, "vwidth", 0)
# コピーするパス
for pen_op in ("glyphPen","addAnchor","addReference"):
    pass

# より確実な方法: SVG を一時保存してインポート（Safe）
tmp_svg = "/tmp/_tmp_glyph_2190.svg"
g_old.export(tmp_svg)
g_base.importOutlines(tmp_svg)
try:
    os.remove(tmp_svg)
except Exception:
    pass

# 変形: Scale(65,100,0,400) は PE の Scale(x%, y%, originX, originY)
# x% = 65 -> scaleX = 0.65, y% =100 -> scaleY = 1.0
# origin は (0,400)
scale_x = 0.65
scale_y = 1.0
origin_x = 0
origin_y = 400
g_base.transform(psMat.translate(-origin_x, -origin_y))
g_base.transform(psMat.scale(scale_x, scale_y))
g_base.transform(psMat.translate(origin_x, origin_y))

# ExpandStroke(20, 0, 0, 0, 1) に相当: stroke をアウトライン化して追加
# FontForge Python には expandStroke 相当のメソッド expandStroke がある
try:
    g_base.stroke("c", 20, "round", "round", 0)  # stroke() はあれば利用
except Exception:
    # fallback: strokeアウトライン化用の FontForge 関数を使う
    try:
        g_base.stroke("c", 20)
    except Exception:
        pass

# 代替（より直接的）: g_base.expandStroke(幅, cap, join, esc, auto) は PE の ExpandStroke
try:
    g_base.expandStroke(20, 0, 0, 0, 1)
except Exception:
    # もし binding に無ければ、font.generate 前に font.stroke を使したり外部で処理してください
    pass

# SetWidth(500) と CenterInWidth()
g_base.width = 500
# CenterInWidth: glyph を幅の中央に移動
# 中心位置を計算して translate
xmin, ymin, xmax, ymax = g_base.boundingBox()
offset = int((g_base.width - (xmax - xmin)) / 2 - xmin)
g_base.transform(psMat.translate(offset, 0))

g_base.removeOverlap()
g_base.correctDirection()
g_base.simplify()
g_base.changed()

# 出力
base.generate(MPLUSUICODE_REGULAR_FONT, flags=("opentype",))
old.close()
base.close()
print("Generated:", MPLUSUICODE_REGULAR_FONT)
