$pdf_mode = 4;                    # LuaLaTeX
$lualatex = 'lualatex --shell-escape %O %S';
$biber = 'biber %O %S';
# NO $aux_dir, NO $out_dir.
# LuaLaTeX on TeX Live does NOT support --aux-directory natively.
# latexmk emulates it by copying files, which breaks makeglossaries.
# Aux files land in repo root. Use `make clean` to tidy up.
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries {
    system("makeglossaries '$_[0]'");
}
