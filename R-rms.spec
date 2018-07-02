#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rms
Version  : 5.1.2
Release  : 13
URL      : https://cran.r-project.org/src/contrib/rms_5.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rms_5.1-2.tar.gz
Summary  : Regression Modeling Strategies
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rms-lib
Requires: R-Hmisc
Requires: R-htmlTable
Requires: R-htmltools
Requires: R-multiwayvcov
Requires: R-polspline
Requires: R-treatSens
BuildRequires : R-Hmisc
BuildRequires : R-TH.data
BuildRequires : R-htmlTable
BuildRequires : R-htmltools
BuildRequires : R-multiwayvcov
BuildRequires : R-polspline
BuildRequires : R-treatSens
BuildRequires : clr-R-helpers

%description
graphics, prediction, and typesetting by storing enhanced model design
	attributes in the fit.  'rms' is a collection of functions that
	assist with and streamline modeling.  It also contains functions for
	binary and ordinal logistic regression models, ordinal models for
  continuous Y with a variety of distribution families, and the Buckley-James
	multiple regression model for right-censored responses, and implements
	penalized maximum likelihood estimation for logistic and ordinary
	linear models.  'rms' works with almost any regression model, but it
	was especially written to work with binary or ordinal regression
	models, Cox regression, accelerated failure time models,
	ordinary linear models,	the Buckley-James model, generalized least
	squares for serially or spatially correlated observations, generalized
	linear models, and quantile regression.

%package lib
Summary: lib components for the R-rms package.
Group: Libraries

%description lib
lib components for the R-rms package.


%prep
%setup -q -c -n rms

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521208656

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521208656
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rms
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rms|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rms/DESCRIPTION
/usr/lib64/R/library/rms/INDEX
/usr/lib64/R/library/rms/Meta/Rd.rds
/usr/lib64/R/library/rms/Meta/demo.rds
/usr/lib64/R/library/rms/Meta/features.rds
/usr/lib64/R/library/rms/Meta/hsearch.rds
/usr/lib64/R/library/rms/Meta/links.rds
/usr/lib64/R/library/rms/Meta/nsInfo.rds
/usr/lib64/R/library/rms/Meta/package.rds
/usr/lib64/R/library/rms/NAMESPACE
/usr/lib64/R/library/rms/NEWS
/usr/lib64/R/library/rms/R/rms
/usr/lib64/R/library/rms/R/rms.rdb
/usr/lib64/R/library/rms/R/rms.rdx
/usr/lib64/R/library/rms/demo/all.R
/usr/lib64/R/library/rms/help/AnIndex
/usr/lib64/R/library/rms/help/aliases.rds
/usr/lib64/R/library/rms/help/paths.rds
/usr/lib64/R/library/rms/help/rms.rdb
/usr/lib64/R/library/rms/help/rms.rdx
/usr/lib64/R/library/rms/html/00Index.html
/usr/lib64/R/library/rms/html/R.css
/usr/lib64/R/library/rms/libs/symbols.rds
/usr/lib64/R/library/rms/tests/Glm.s
/usr/lib64/R/library/rms/tests/Gls.s
/usr/lib64/R/library/rms/tests/Predict.s
/usr/lib64/R/library/rms/tests/Rq.s
/usr/lib64/R/library/rms/tests/Rq2.s
/usr/lib64/R/library/rms/tests/anova-ols-mult-impute.r
/usr/lib64/R/library/rms/tests/bj.r
/usr/lib64/R/library/rms/tests/bootcov.r
/usr/lib64/R/library/rms/tests/bplot.r
/usr/lib64/R/library/rms/tests/contrast.r
/usr/lib64/R/library/rms/tests/cph.s
/usr/lib64/R/library/rms/tests/cph2.s
/usr/lib64/R/library/rms/tests/cph3.r
/usr/lib64/R/library/rms/tests/cph4.r
/usr/lib64/R/library/rms/tests/cphtdc.r
/usr/lib64/R/library/rms/tests/examples.Rmd
/usr/lib64/R/library/rms/tests/ggplot.Predict.Rd.timing.r
/usr/lib64/R/library/rms/tests/ggplot2-without-ggplot.Predict.r
/usr/lib64/R/library/rms/tests/ggplot2.r
/usr/lib64/R/library/rms/tests/ggplot2b.r
/usr/lib64/R/library/rms/tests/ggplot3.r
/usr/lib64/R/library/rms/tests/ggplotly.Rmd
/usr/lib64/R/library/rms/tests/latex.r
/usr/lib64/R/library/rms/tests/lrm.ols.penalty.r
/usr/lib64/R/library/rms/tests/lrm.ordinal.s
/usr/lib64/R/library/rms/tests/lrm.s
/usr/lib64/R/library/rms/tests/lrmMean.s
/usr/lib64/R/library/rms/tests/mice.r
/usr/lib64/R/library/rms/tests/model.matrix.s
/usr/lib64/R/library/rms/tests/nomogram.r
/usr/lib64/R/library/rms/tests/offset.r
/usr/lib64/R/library/rms/tests/ols.penalty.r
/usr/lib64/R/library/rms/tests/ols.r
/usr/lib64/R/library/rms/tests/orm-bootcov.r
/usr/lib64/R/library/rms/tests/orm-example.r
/usr/lib64/R/library/rms/tests/orm-profile.r
/usr/lib64/R/library/rms/tests/orm-residuals.r
/usr/lib64/R/library/rms/tests/orm.s
/usr/lib64/R/library/rms/tests/orm2.s
/usr/lib64/R/library/rms/tests/orm3.r
/usr/lib64/R/library/rms/tests/orm4.r
/usr/lib64/R/library/rms/tests/pentrace.s
/usr/lib64/R/library/rms/tests/perlcode.s
/usr/lib64/R/library/rms/tests/plot.Predict.s
/usr/lib64/R/library/rms/tests/plotly-Predict.r
/usr/lib64/R/library/rms/tests/predictrms.s
/usr/lib64/R/library/rms/tests/psm.s
/usr/lib64/R/library/rms/tests/psm2.s
/usr/lib64/R/library/rms/tests/psm3.s
/usr/lib64/R/library/rms/tests/qt50.rda
/usr/lib64/R/library/rms/tests/rcs.r
/usr/lib64/R/library/rms/tests/rms.r
/usr/lib64/R/library/rms/tests/rms2.r
/usr/lib64/R/library/rms/tests/robcov.r
/usr/lib64/R/library/rms/tests/robcov2.r
/usr/lib64/R/library/rms/tests/sampledf.rda
/usr/lib64/R/library/rms/tests/scale.r
/usr/lib64/R/library/rms/tests/simult.s
/usr/lib64/R/library/rms/tests/strat.model.matrix.r
/usr/lib64/R/library/rms/tests/summary.r
/usr/lib64/R/library/rms/tests/survest.r
/usr/lib64/R/library/rms/tests/survfit.cph.s
/usr/lib64/R/library/rms/tests/survfit.timedep.s
/usr/lib64/R/library/rms/tests/survplot.s
/usr/lib64/R/library/rms/tests/survplot2.r
/usr/lib64/R/library/rms/tests/survplotCompete.r
/usr/lib64/R/library/rms/tests/survplotp.r
/usr/lib64/R/library/rms/tests/val.prob.r
/usr/lib64/R/library/rms/tests/val.surv.s
/usr/lib64/R/library/rms/tests/validate.cph.s
/usr/lib64/R/library/rms/tests/validate.ols.r
/usr/lib64/R/library/rms/tests/validate.rpart.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rms/libs/rms.so
/usr/lib64/R/library/rms/libs/rms.so.avx2
/usr/lib64/R/library/rms/libs/rms.so.avx512
