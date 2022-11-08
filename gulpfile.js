const { src, dest, watch, series } = require('gulp');
const sass = require('gulp-sass')(require('node-sass'));
const fileinclude = require('gulp-file-include');

// compiling SASS into CSS
function scss() {
    return src('src/scss/*.scss')
    .pipe(sass({outputStyle: 'compact'}).on('error', sass.logError))
    .pipe(dest('zaid/static/css'))
}

function scripts(){
    return src(['src/js/*.js'])
    .pipe(fileinclude({
      prefix: '@@',
      basepath: '@file',
      context: {
        build: 'dist',
        nodeRoot: '../..'
      }
    }))
    .pipe(dest('zaid/static/js'))
}


// START DEVELOPING
exports.develop = function() {
	watch(['src/scss/*.scss', 'src/scss/**'], scss)
	watch(['src/js/*.js', 'src/js/**'], scripts)
};

exports.build = series(scss, scripts);
