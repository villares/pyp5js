from pyp5js import templates_renderers as renderers
from pyp5js.sketch import Sketch
from pyp5js.config.fs import PYP5JS_FILES

from .fixtures import sketch

def test_get_sketch_index_content(sketch):
    expected_template = renderers.templates.get_template('transcrypt/index.html')
    expected_content = expected_template.render({
        'sketch_name': sketch.sketch_name,
        "p5_js_url": sketch.STATIC_NAME + "/p5.js",
        "sketch_js_url": sketch.TARGET_NAME + "/target_sketch.js",
    })

    assert expected_content == renderers.get_sketch_index_content(sketch)


def test_get_target_sketch_content(sketch):
    with open(sketch.sketch_py, 'w') as fd:
        fd.write('content')

    expected_template = renderers.templates.get_template('transcrypt/target_sketch.py.template')
    expected_content = expected_template.render({
        'sketch_name': sketch.sketch_name,
        'sketch_content': 'content'
    })
    content = renderers.get_target_sketch_content(sketch)

    assert expected_content == content
    assert "import foo as source_sketch" in content
