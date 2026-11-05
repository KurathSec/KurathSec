<pre>
    __ __  __  __  ____    ___   ______  __  __  _____   ______  ______
   / //_/ / / / / / __ \  /   | /_  __/ / / / / / ___/  / ____/ / ____/
  / ,&lt;   / / / / / /_/ / / /| |  / /   / /_/ /  \__ \  / __/   / /
 / /| | / /_/ / / _, _/ / ___ | / /   / __  /  ___/ / / /___  / /___
/_/ |_| \____/ /_/ |_| /_/  |_|/_/   /_/ /_/  /____/ /_____/  \____/

software, and the instruments that check it

5         6         7         8         9         10        11        12
|---------|---------|---------|---------|---------|---------|---------|
              |        |        |        |        #        |        |
              0        1        2        3        4        5        6

--[ .plan ]-------------------------------------------------------------

security and correctness in cryptographic and systems code, and the
tools that measure it. most of my work starts with a narrow question and
ends with a result someone else can rerun and, where it turns up
something useful, a patch or a report to the project involved.

--[ upstream ]----------------------------------------------------------

[merged] openssl       <a href="https://github.com/openssl/openssl/pull/33285">#33285</a>     RAND(7): a restore from a saved image
                                  is not detected. all active branches
[merged] botan         <a href="https://github.com/randombit/botan/pull/6049">#6049</a>      fork safety guidance for snapshot and
                                  checkpoint restores
[merged] circl         <a href="https://github.com/cloudflare/circl/pull/704">#704</a>       wycheproof ml-kem vectors: 1,725 cases
[merged] pmd           <a href="https://github.com/pmd/pmd/pull/6883">#6883</a>      cognitive complexity counts java
                                  switch expressions. released in 7.27.0
[tested] botan         <a href="https://github.com/randombit/botan/pull/6054">#6054</a>      maintainer's vm rollback fix: repeats
                                  at its parent (15/15 pairs), distinct
                                  with it (30/30)
[review] openssl       <a href="https://github.com/openssl/openssl/pull/33286">#33286</a>     reseed provider drbgs when the linux
                                  vmclock generation counter changes
[review] openssl       <a href="https://github.com/openssl/openssl/pull/33508">#33508</a>     RAND(7): a fork that keeps its pid
[review] circl         <a href="https://github.com/cloudflare/circl/pull/705">#705</a>       wycheproof x25519 and x448 vectors
[review] cargo-mutants <a href="https://github.com/sourcefrog/cargo-mutants/pull/655">#655</a>       --stop-on-missed: stop after the first
                                  missed mutant
[report] acvp-server   <a href="https://github.com/usnistgov/ACVP-Server/issues/468">#468</a> <a href="https://github.com/usnistgov/ACVP-Server/issues/470">#470</a>  gaps between what fips 203 and 204
                                  mandate and what the validation
                                  vectors can exercise. root causes and
                                  measurements on <a href="https://github.com/usnistgov/ACVP-Server/issues/460">#460</a>, <a href="https://github.com/usnistgov/ACVP-Server/issues/462">#462</a>, <a href="https://github.com/usnistgov/ACVP-Server/pull/464">#464</a>
[report] criu          <a href="https://github.com/checkpoint-restore/criu/issues/3237">#3237</a>      dump fails on aarch64 when a process
                                  maps /dev/vmclock0; traced the cause
[report] rand          <a href="https://github.com/rust-random/rand/issues/1843">#1843</a>      threadrng after a restore; docs
                                  updated in <a href="https://github.com/rust-random/rand/pull/1844">#1844</a>
[report] node          <a href="https://github.com/nodejs/node/issues/66880">#66880</a>     crypto random functions after a
                                  restore; docs request

--[ instruments ]-------------------------------------------------------

<a href="https://github.com/KurathSec/codecaliper">codecaliper</a>          how readable and complex code is, for python, java,
                     and go. every number cites the versioned rule and
                     grammar behind it
                     [<a href="https://kurathsec.github.io/codecaliper/">docs</a>] [<a href="https://pypi.org/project/codecaliper/">pypi</a>] [<a href="https://doi.org/10.5281/zenodo.21312527">doi</a>]
<a href="https://github.com/KurathSec/limen">limen</a>                whether a benchmark comparison clears its own noise
                     floor, from repeated runs, with a ci gate
                     [<a href="https://kurathsec.github.io/limen/">docs</a>] [<a href="https://pypi.org/project/limen-eval/">pypi</a>] [<a href="https://doi.org/10.5281/zenodo.21699645">doi</a>] [<a href="https://github.com/KurathSec/limen#github-action">action</a>]
<a href="https://github.com/KurathSec/cupel">cupel</a>                which clauses of fips 203 and 204 the acvp
                     validation vectors exercise, neutralising one check
                     at a time
                     [<a href="https://doi.org/10.5281/zenodo.21880235">doi</a>]

--[ systems ]-----------------------------------------------------------

<a href="https://github.com/KurathSec/gm-recomp">gm-recomp</a>            windows gamemaker games in desktop browsers, from
                     their original executables: x86 recompiled to
                     webassembly, windows apis in rust. ships an
                     embeddable player
                     [<a href="https://github.com/KurathSec/gm-recomp/releases">releases</a>]
<a href="https://github.com/KurathSec/fangame-archive">fangame-archive</a>      serverless catalog and reviews for i wanna be the
                     guy fangames: 20,000+ games, 156,000 reviews, 8
                     languages, on cloudflare pages, d1, r2, kv
<a href="https://github.com/KurathSec/Spaghetti-Architect">spaghetti-architect</a>  one program description compiled to python,
                     javascript, go, java, and c++, each run to check
                     they match. also generates labelled llm benchmarks
                     [<a href="https://arxiv.org/abs/2607.18642">arxiv</a>] [<a href="https://doi.org/10.5281/zenodo.21033174">doi</a>]

--[ stack ]-------------------------------------------------------------

domain     cybersecurity, applied cryptography, fips 203/204
language   rust, c, go, python, java, javascript
runtime    webassembly, webgl2, x86, linux, qemu/kvm, firecracker, criu
method     mutation testing, differential testing, static analysis
platform   cloudflare workers, react, sqlite, github actions

--[ 88x31 ]-------------------------------------------------------------

<a href="https://github.com/KurathSec/gm-recomp"><img src="assets/gm-recomp.gif" width="88" height="31" alt="gm-recomp"></a> <a href="https://github.com/KurathSec/fangame-archive"><img src="assets/fangame-archive.gif" width="88" height="31" alt="Fangame Archive"></a> <a href="https://github.com/KurathSec/Spaghetti-Architect"><img src="assets/spaghetti-architect.gif" width="88" height="31" alt="Spaghetti Architect"></a> <a href="https://github.com/KurathSec/codecaliper"><img src="assets/codecaliper.gif" width="88" height="31" alt="codecaliper"></a> <a href="https://github.com/KurathSec/limen"><img src="assets/limen.gif" width="88" height="31" alt="limen"></a> <a href="https://github.com/KurathSec/cupel"><img src="assets/cupel.gif" width="88" height="31" alt="cupel"></a>
<a href="https://github.com/openssl/openssl/pull/33285"><img src="assets/merged-openssl.gif" width="88" height="31" alt="merged in OpenSSL"></a> <a href="https://github.com/randombit/botan/pull/6049"><img src="assets/merged-botan.gif" width="88" height="31" alt="merged in Botan"></a> <a href="https://github.com/cloudflare/circl/pull/704"><img src="assets/merged-circl.gif" width="88" height="31" alt="merged in CIRCL"></a> <a href="https://github.com/pmd/pmd/pull/6883"><img src="assets/merged-pmd.gif" width="88" height="31" alt="merged in PMD"></a> <a href="https://arxiv.org/abs/2607.18642"><img src="assets/arxiv.gif" width="88" height="31" alt="arXiv 2607.18642"></a> <a href="https://github.com/KurathSec/KurathSec"><img src="assets/view-source.gif" width="88" height="31" alt="view source"></a>

kurathsec@github:~$ <img src="assets/cursor.gif" width="8" height="14" alt="_">
</pre>
