all: build/MPLUSUI-Regular.ttf build/MPLUSUI-Bold.ttf build/MPLUSUIMono-Regular.ttf build/MPLUSUIMono-Bold.ttf build/MPLUSUICode-Regular.ttf build/MPLUSUICode-Bold.ttf

install: all
	cp build/MPLUSUI*.ttf ~/.local/share/fonts/
	fc-cache -fr

build/MPLUSUI-Regular.ttf: MPLUSUI-Regular.pe build/MPLUS1-Regular.ttf build/MPLUS1p-Regular.ttf
	fontforge MPLUSUI-Regular.pe build/MPLUSUI-Regular.ttf build/MPLUS1-Regular.ttf build/MPLUS1p-Regular.ttf

build/MPLUSUI-Bold.ttf: MPLUSUI-Bold.pe build/MPLUS1-Bold.ttf build/MPLUS1p-Bold.ttf
	fontforge MPLUSUI-Bold.pe build/MPLUSUI-Bold.ttf build/MPLUS1-Bold.ttf build/MPLUS1p-Bold.ttf

build/MPLUSUIMono-Regular.ttf: MPLUSUIMono-Regular.pe build/MPLUS1Code-Regular.ttf build/MPLUS1p-Regular.ttf build/MPLUS1-Regular.ttf build/VL-Gothic-Regular.ttf
	fontforge MPLUSUIMono-Regular.pe build/MPLUSUIMono-Regular.ttf build/MPLUS1Code-Regular.ttf build/MPLUS1p-Regular.ttf build/MPLUS1-Regular.ttf build/VL-Gothic-Regular.ttf

build/MPLUSUIMono-Bold.ttf: MPLUSUIMono-Bold.pe build/MPLUS1Code-Bold.ttf build/MPLUS1p-Bold.ttf build/MPLUS1-Bold.ttf
	fontforge MPLUSUIMono-Bold.pe build/MPLUSUIMono-Bold.ttf build/MPLUS1Code-Bold.ttf build/MPLUS1p-Bold.ttf build/MPLUS1-Bold.ttf

build/MPLUSUICode-Regular.ttf: MPLUSUICode-Regular.pe build/MPLUS1Code-Regular.ttf build/MPLUS1p-Regular.ttf build/MPLUS1-Regular.ttf build/VL-Gothic-Regular.ttf
	fontforge MPLUSUICode-Regular.pe build/MPLUSUICode-Regular.ttf build/MPLUS1Code-Regular.ttf build/MPLUS1p-Regular.ttf build/MPLUS1-Regular.ttf build/VL-Gothic-Regular.ttf

build/MPLUSUICode-Bold.ttf: MPLUSUICode-Bold.pe build/MPLUS1Code-Bold.ttf build/MPLUS1p-Bold.ttf build/MPLUS1-Bold.ttf
	fontforge MPLUSUICode-Bold.pe build/MPLUSUICode-Bold.ttf build/MPLUS1Code-Bold.ttf build/MPLUS1p-Bold.ttf build/MPLUS1-Bold.ttf

build/MPLUS1-Regular.ttf: ~/.local/share/fonts/MPLUS1-Regular.ttf
	cp ~/.local/share/fonts/MPLUS1-Regular.ttf build/

build/MPLUS1-Bold.ttf: ~/.local/share/fonts/MPLUS1-Bold.ttf
	cp ~/.local/share/fonts/MPLUS1-Bold.ttf build/

build/MPLUS1Code-Regular.ttf: ~/.local/share/fonts/MPLUS1Code-Regular.ttf
	cp ~/.local/share/fonts/MPLUS1Code-Regular.ttf build/

build/MPLUS1Code-Bold.ttf: ~/.local/share/fonts/MPLUS1Code-Bold.ttf
	cp ~/.local/share/fonts/MPLUS1Code-Bold.ttf build/

build/MPLUS1p-Regular.ttf: ~/.local/share/fonts/MPLUS1p-Regular.ttf
	cp ~/.local/share/fonts/MPLUS1p-Regular.ttf build/

build/MPLUS1p-Bold.ttf: ~/.local/share/fonts/MPLUS1p-Bold.ttf
	cp ~/.local/share/fonts/MPLUS1p-Bold.ttf build/

build/VL-Gothic-Regular.ttf: /usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf
	cp /usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf build/
