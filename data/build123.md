(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
<p align="center">
    <img alt="build123d logo" src="https://github.com/gumyr/build123d/raw/dev/docs/assets/build123d_logo/logo-banner.svg">
</p>

[![Documentation Status](https://readthedocs.org/projects/build123d/badge/?version=latest)](https://build123d.readthedocs.io/en/latest/?badge=latest)
[![tests](https://github.com/gumyr/build123d/actions/workflows/test.yml/badge.svg)](https://github.com/gumyr/build123d/actions/workflows/test.yml)
[![pylint](https://github.com/gumyr/build123d/actions/workflows/lint.yml/badge.svg)](https://github.com/gumyr/build123d/actions/workflows/lint.yml)
[![mypy](https://github.com/gumyr/build123d/actions/workflows/mypy.yml/badge.svg)](https://github.com/gumyr/build123d/actions/workflows/mypy.yml)
[![codecov](https://codecov.io/gh/gumyr/build123d/branch/dev/graph/badge.svg)](https://codecov.io/gh/gumyr/build123d)

![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![PyPI version](https://img.shields.io/pypi/v/build123d.svg)](https://pypi.org/project/build123d/)
[![Downloads](https://pepy.tech/badge/build123d)](https://pepy.tech/project/build123d)
[![Downloads/month](https://pepy.tech/badge/build123d/month)](https://pepy.tech/project/build123d)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/build123d.svg)](https://pypi.org/project/build123d/)
[![DOI](https://zenodo.org/badge/510925389.svg)](https://doi.org/10.5281/zenodo.14872322)


Build123d is a Python-based, parametric [boundary representation (BREP)][BREP] modeling framework for 2D and 3D CAD. Built on the [Open Cascade] geometric kernel, it provides a clean, fully Pythonic interface for creating precise models suitable for 3D printing, CNC machining, laser cutting, and other manufacturing processes. Models can be exported to popular CAD tools such as [FreeCAD] and SolidWorks.

Designed for modern, maintainable CAD-as-code, build123d combines clear architecture with expressive, algebraic modeling. It offers:
- Minimal or no internal state depending on mode,
- Explicit 1D, 2D, and 3D geometry classes with well-defined operations,
- Extensibility through subclassing and functional composition—no monkey patching,
- Standards-compliant code (PEP 8, mypy, pylint) with rich pylance type hints,
- Deep Python integration—selectors as lists, locations as iterables, and natural conversions (Solid(shell), tuple(Vector)),
- Operator-driven modeling (obj += sub_obj, Plane.XZ * Pos(X=5) * Rectangle(1, 1)) for algebraic, readable, and composable design logic.

The result is a framework that feels native to Python while providing the full power of OpenCascade geometry underneath.

The documentation for **build123d** can be found at [readthedocs](https://build123d.readthedocs.io/en/latest/index.html).

There is a [***Discord***](https://discord.com/invite/Bj9AQPsCfx) server (shared with [CadQuery]) where you can ask for help in the build123d channel.

The recommended method for most users to install **build123d** is:

```
pip install build123d
```

To get the latest non-released version of **build123d** one can install from GitHub using one of the following two commands:

Linux/MacOS:

```
python3 -m pip install git+https://github.com/gumyr/build123d
```

Windows:

```
python -m pip install git+https://github.com/gumyr/build123d
```

If you receive errors about conflicting dependencies, you can retry the installation after having upgraded pip to the latest version with the following command:
```
python3 -m pip install --upgrade pip
```

Development install:

```
git clone https://github.com/gumyr/build123d.git
cd build123d
python3 -m pip install -e .
```

Further installation instructions are available (e.g. Poetry) see the [installation section on readthedocs](https://build123d.readthedocs.io/en/latest/installation.html).

Attribution:

Build123d was originally derived from portions of the [CadQuery] codebase but has since been extensively refactored and restructured into an independent system.

[BREP]: https://en.wikipedia.org/wiki/Boundary_representation
[CadQuery]: https://cadquery.readthedocs.io/en/latest/index.html
[FreeCAD]: https://www.freecad.org/
[Open Cascade]: https://dev.opencascade.org/



================================================
FILE: CITATION.cff
================================================
cff-version: 1.2.0
message: "If you use build123d in your research, please cite it using the following information."
title: "build123d: A Python-based parametric CAD library"
version: "0.9.1"
doi: "10.5281/zenodo.14872323"
authors:
  - name: "Roger Maitland"
    affiliation: "Independent Developer"
date-released: "2025-02-14"
repository-code: "https://github.com/gumyr/build123d"
license: "Apache-2.0"
keywords:
  - CAD
  - Python
  - OpenCascade
  - Parametric Design



================================================
FILE: Citation.md
================================================
# Citation

If you use **build123d** in your research, please cite:

Roger Maitland. **"build123d: A Python-based parametric CAD library"**. Version 0.9.1, 2025.  
DOI: [10.5281/zenodo.14872323](https://doi.org/10.5281/zenodo.14872323)  
Source Code: [GitHub](https://github.com/gumyr/build123d)

## BibTeX Entry

```bibtex
@software{build123d,
  author = {Roger Maitland},
  title = {build123d: A Python-based parametric CAD library},
  year = {2025},
  version = {0.9.1},
  doi = {10.5281/zenodo.14872323},
  url = {https://github.com/gumyr/build123d}
}


================================================
FILE: CONTRIBUTING.md
================================================
When writing code for inclusion in build123d please add docs and
tests, ensure they build and pass, and ensure that `pylint` and `mypy`
are happy with your code.

- Install `pip` following their [documentation](https://pip.pypa.io/en/stable/installation/).
- Install development dependencies: `pip install -e .[development]`
- Install docs dependencies: `pip install -e .[docs]`
- Install `build123d` in editable mode from current dir:  `pip install -e .`
- Run tests with: `python -m pytest -n auto`
- Build docs with: `cd docs && make html`
- Check added files' style with: `pylint <path/to/file.py>` 
- Check added files' type annotations with: `mypy <path/to/file.py>`
- Run black formatter against files' changed: `black --config pyproject.toml <path/to/file.py>` (where the pyproject.toml is from this project's repository)



================================================
FILE: LICENSE
================================================

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.



================================================
FILE: MANIFEST.in
================================================
# exclude build123d._dev from sdists
prune src/build123d/_dev


================================================
FILE: mypy.ini
================================================
# Global options:

[mypy]

[mypy-anytree.*]
ignore_missing_imports = True

[mypy-build123d.topology.jupyter_tools.*]
ignore_missing_imports = True

[mypy-cadquery-ocp-stubs.*]
ignore_missing_imports = True

[mypy-IPython.*]
ignore_missing_imports = True

[mypy-numpy.*]
ignore_missing_imports = True

[mypy-OCP.*]
ignore_missing_imports = True

[mypy-ocpsvg.*]
ignore_missing_imports = True

[mypy-scipy.*]
ignore_missing_imports = True

[mypy-svgpathtools.*]
ignore_missing_imports = True

[mypy-trianglesolver.*]
ignore_missing_imports = True

[mypy-vtkmodules.*]
ignore_missing_imports = True

[mypy-ezdxf.*]
ignore_missing_imports = True

[mypy-setuptools_scm.*]
ignore_missing_imports = True

[mypy-lib3mf.*]
ignore_missing_imports = True



================================================
FILE: NOTICE
================================================
build123d
Copyright (c) 2022–2025 The build123d Contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

-------------------------------------------------------------------------------

This project was originally derived from portions of the CadQuery codebase
(https://github.com/CadQuery/cadquery) but has since been extensively
refactored and restructured into an independent system.
CadQuery is licensed under the Apache License, Version 2.0.



================================================
FILE: partcad.yaml
================================================
# This is a declaration of a PartCAD package.
# See https://partcad.org/ and https://github.com/openvmp/partcad for more information.

desc: Examples of parts defined with build123d
url: https://github.com/gumyr/build123d
partcad: ">=0.5.22"
pythonRequirements:
  - ocp_vscode
  - build123d>=0.7.1

sketches:
  examples/clock:
    type: build123d
    desc: Clock Face (Builder mode)

  examples/clock_algebra:
    type: build123d
    desc: Clock Face (Algebra mode)

  examples/python_logo:
    type: build123d
    desc: This python module creates the Python logo as a Sketch object
    show: PythonLogo(10)

  examples/shamrock:
    type: build123d
    desc: Adds a four leaf clover

parts:
  examples/benchy:
    type: build123d
    desc: STL import and edit example (Builder mode)
    cwd: examples

  examples/boxes_on_faces:
    type: build123d
    desc: Demo adding features to multiple faces in one operation (Builder mode)

  examples/boxes_on_faces_algebra:
    type: build123d
    desc: Demo adding features to multiple faces in one operation (Algebra mode)

  examples/build123d_customizable_logo:
    type: build123d
    desc: This example creates the build123d customizable logo (Builder mode)

  examples/build123d_customizable_logo_algebra:
    type: build123d
    desc: This example creates the build123d customizable logo (Algebra mode)

  examples/build123d_logo:
    type: build123d
    desc: This example creates the former build123d logo (Builder mode).

  examples/build123d_logo_algebra:
    type: build123d
    desc: This example creates the former build123d logo (Algebra mode).

  # `canadian_flag` can't be a PartCAD part as it doesn't have volume, and it can't be a sketch as it's not plain
  # examples/canadian_flag:
  #   type: build123d
  #   desc: Canadian Flag Blowing in The Wind (Builder mode)

  # examples/canadian_flag_algebra:
  #   type: build123d
  #   desc: Canadian Flag Blowing in The Wind (Algebra mode)

  examples/circuit_board:
    type: build123d
    desc: This example demonstrates placing holes around a part (Builder mode)

  examples/circuit_board_algebra:
    type: build123d
    desc: This example demonstrates placing holes around a part (Algebra mode)

  examples/custom_sketch_objects:
    type: build123d
    desc: |
      This example demonstrates the creation of a Playing Card storage box with
      user generated custom BuildSketch objects. Four new BuildSketch objects are
      created: Club, Spade, Heart, and Diamond, which are then used to punch
      holes into the top of the box's lid. (Builder mode)

  examples/custom_sketch_objects_algebra:
    type: build123d
    desc: |
      This example demonstrates the creation of a Playing Card storage box with
      user generated custom BuildSketch objects. Four new BuildSketch objects are
      created: Club, Spade, Heart, and Diamond, which are then used to punch
      holes into the top of the box's lid. (Algebra mode)

  examples/din_rail:
    type: build123d
    desc: |
      This example demonstrates multiple vertex filtering techniques including
      a fully custom filter. It also shows how a workplane can be replaced
      with another in a different orientation for further work. (Builder mode)
    parameters:
      rail_length:
        type: int
        desc: Length of the DIN rail
        default: 1000

  examples/din_rail_algebra:
    type: build123d
    desc: |
      This example demonstrates multiple vertex filtering techniques including
      a fully custom filter. It also shows how a workplane can be replaced
      with another in a different orientation for further work. (Algebra mode)
    parameters:
      rail_length:
        type: int
        desc: Length of the DIN rail
        default: 1000

  examples/dual_color_3mf:
    type: build123d
    desc: |
      The 3MF mesh format supports multiple colors which can be used on
      multi-filament 3D printers. This example creates an tile pattern
      with an insert and background in different colors.

  examples/extrude:
    type: build123d
    desc: |
      This example demonstrates multiple uses of Extrude cumulating in
      the design of a key cap. (Builder mode)

  examples/extrude_algebra:
    type: build123d
    desc: |
      This example demonstrates multiple uses of Extrude cumulating in
      the design of a key cap. (Algebra mode)

  examples/handle:
    type: build123d
    desc: |
      This example demonstrates multisection sweep creating a drawer handle (Builder mode)

  examples/handle_algebra:
    type: build123d
    desc: |
      This example demonstrates multisection sweep creating a drawer handle (Algebra mode)

  examples/heat_exchanger:
    type: build123d
    desc: |
      This example creates a model of a parametric heat exchanger core (Builder mode)

  examples/heat_exchanger_algebra:
    type: build123d
    desc: |
      This example creates a model of a parametric heat exchanger core (Algebra mode)

  examples/holes:
    type: build123d
    desc: This example demonstrates multiple hole types (Builder mode)

  examples/holes_algebra:
    type: build123d
    desc: This example demonstrates multiple hole types (Algebra mode)

  examples/intersecting_chamfers:
    type: build123d
    desc: Intersecting chamfers (Builder mode)

  examples/intersecting_chamfers_algebra:
    type: build123d
    desc: Intersecting chamfers (Algebra mode)

  examples/intersecting_pipes:
    type: build123d
    desc: |
      This example demonstrates working on multiple planes created from object
      faces and using a Select.LAST selector to return edges to be filleted.

  examples/joints:
    type: build123d
    desc: Experimental Joint development file (Builder mode)

  examples/joints_algebra:
    type: build123d
    desc: Experimental Joint development file (Algebra mode)

  examples/key_cap:
    type: build123d
    url: https://www.cherrymx.de/en/dev.html
    desc: |
      This example demonstrates the design of a Cherry MX key cap by using
      extrude with a taper and extrude until next (Builder mode)

  examples/key_cap_algebra:
    type: build123d
    url: https://www.cherrymx.de/en/dev.html
    desc: |
      This example demonstrates the design of a Cherry MX key cap by using
      extrude with a taper and extrude until next (Algebra mode)

  examples/lego:
    type: build123d
    cwd: docs
    desc: |
      This example creates a model of a double wide lego block with a
      parametric length (pip_count) (Builder mode)

  examples/lego_algebra:
    type: build123d
    cwd: docs
    desc: |
      This example creates a model of a double wide lego block with a
      parametric length (pip_count) (Algebra mode)

  examples/loft:
    type: build123d
    desc: |
      This example demonstrates lofting a set of sketches, selecting
      the top and bottom by type, and shelling (Builder mode)

  examples/loft_algebra:
    type: build123d
    desc: |
      This example demonstrates lofting a set of sketches, selecting
      the top and bottom by type, and shelling (Algebra mode)

  examples/maker_coin:
    type: build123d
    desc: |
      This example creates the maker coin as defined by Angus on the Maker's Muse
      YouTube channel

  examples/mixed_algebra_context:
    type: build123d
    desc: Mix content and algebra api

  examples/multiple_workplanes:
    type: build123d
    desc: Multiple workplanes (Builder mode)

  examples/multiple_workplanes_algebra:
    type: build123d
    desc: Multiple workplanes (Algebra mode)

  examples/packed_boxes:
    type: build123d
    desc: Demo packing a bunch of boxes in 2D
    cwd: examples
    patch:
      "\\Z": "\\nshow_object(packed)"
      # "\\Z": "\\nshow_object(test_boxes)"

  examples/pegboard_j_hook:
    type: build123d
    desc: |
      This example creates a model of j-shaped pegboard hook commonly used
      for organization of tools in garages (Builder mode)

  examples/pegboard_j_hook_algebra:
    type: build123d
    desc: |
      This example creates a model of j-shaped pegboard hook commonly used
      for organization of tools in garages (Algebra mode)

  examples/pillow_block:
    type: build123d
    desc: This example demonstrates placing holes in a part in a rectangular array (Builder mode)

  examples/pillow_block_algebra:
    type: build123d
    desc: This example demonstrates placing holes in a part in a rectangular array (Algebra mode)

  examples/platonic_solids:
    type: build123d
    desc: This example creates a custom Part object PlatonicSolid

  examples/playing_cards:
    type: build123d
    desc: |
      This example demonstrates user generated custom BuildSketch objects.
      The script defines five classes: Club, Spade, Heart, Diamond, and PlayingCard
      in addition to a two part playing card box which has suit cutouts in the
      lid.

  examples/projection:
    type: build123d
    desc: Projection examples (Builder mode)

  examples/projection_algebra:
    type: build123d
    desc: Projection examples (Algebra mode)

  # `roller_coaster` can't be a PartCAD part as it doesn't have volume, and it can't be a sketch as it's not plain
  # examples/roller_coaster:
  #   type: build123d
  #   desc: |
  #     This example demonstrates building complex 3D lines by "snapping"
  #     features to existing objects (Builder mode)

  # examples/roller_coaster_algebra:
  #   type: build123d
  #   desc: |
  #     This example demonstrates building complex 3D lines by "snapping"
  #     features to existing objects (Algebra mode)

  examples/stud_wall:
    type: build123d
    desc: |
      This example builds stud walls from dimensional lumber as an assembly
      with the parts positioned with RigidJoints

  examples/tea_cup:
    type: build123d
    desc: |
      This example demonstrates the creation a tea cup, which serves as an example of 
      constructing complex, non-flat geometrical shapes programmatically (Builder mode)

  examples/tea_cup_algebra:
    type: build123d
    desc: |
      This example demonstrates the creation a tea cup, which serves as an example of 
      constructing complex, non-flat geometrical shapes programmatically (Algebra mode)

  examples/vase:
    type: build123d
    desc: |
      This example demonstrates the build123d techniques involving the creation of a vase. 
      Specifically, it showcases the processes of revolving a sketch, shelling 
      (creating a hollow object by removing material from its interior), and 
      selecting edges by position range and type for the application of fillets 
      (rounding off the edges). (Builder mode)

  examples/vase_algebra:
    type: build123d
    desc: |
      This example demonstrates the build123d techniques involving the creation of a vase. 
      Specifically, it showcases the processes of revolving a sketch, shelling 
      (creating a hollow object by removing material from its interior), and 
      selecting edges by position range and type for the application of fillets 
      (rounding off the edges). (Algebra mode)



================================================
FILE: pyproject.toml
================================================
[build-system]

requires = [
    "setuptools>=45",
    "wheel",
    "setuptools_scm[toml]>=6.2",
]

build-backend = "setuptools.build_meta"

[project]
name = "build123d"
dynamic = ["version"]
authors = [
    {name = "Roger Maitland", email = "gumyr9@gmail.com"},
]
description = "A python CAD programming library"
readme = "README.md"
requires-python = ">= 3.10, < 3.14"
keywords = [
    "3d models",
    "3d printing",
    "3d",
    "brep",
    "cad",
    "cadquery",
    "opencascade",
    "python",
]
license = {text = "Apache-2.0"}
classifiers = [
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
]

dependencies = [
    "cadquery-ocp >= 7.8, < 7.9",
    "typing_extensions >= 4.6.0, < 5",
    "numpy >= 2, < 3",
    "svgpathtools >= 1.5.1, < 2",
    "anytree >= 2.8.0, < 3",
    "ezdxf >= 1.1.0, < 2",
    "ipython >= 8.0.0, < 10",
    "lib3mf >= 2.4.1",
    "ocpsvg >= 0.5, < 0.6",
    "ocp_gordon >= 0.1.17",
    "trianglesolver",
    "sympy",
    "scipy",
    "webcolors ~= 24.8.0",
]

[project.urls]
"Homepage" = "https://github.com/gumyr/build123d"
"Documentation" = "https://build123d.readthedocs.io/en/latest/index.html"
"Bug Tracker" = "https://github.com/gumyr/build123d/issues"
"Citation" = "https://doi.org/10.5281/zenodo.14872323"

[project.optional-dependencies]
# enable the optional ocp_vscode visualization package
ocp_vscode = [
    "ocp_vscode",
]

# development dependencies
development = [
    "black",
    "mypy",
    "pylint",
    "pytest",
    "pytest-benchmark",
    "pytest-cov",
    "pytest-xdist",
    "wheel",
]

# typing stubs for the OCP CAD kernel
stubs = [
    "cadquery-ocp-stubs >= 7.8, < 7.9",
]

# dependencies to build the docs
docs = [
    "sphinx==8.1.3", # pin for stability of docs builds
    "sphinx-design",
    "sphinx-copybutton",
    "sphinx-hoverxref",
    "sphinx-rtd-theme",
    "sphinx_autodoc_typehints",
]

# all dependencies
all = [
    "build123d[ocp_vscode]",
    "build123d[development]",
    "build123d[docs]",
    # "build123d[stubs]", # excluded for now as mypy fails
]

[tool.setuptools.packages.find]
where = ["src"]
# exclude build123d._dev from wheels
exclude = ["build123d._dev"]

[tool.setuptools_scm]
write_to = "src/build123d/_version.py"

[tool.black]
target-version = ["py310", "py311", "py312", "py313"]
line-length = 88



================================================
FILE: .pylintrc
================================================
[MAIN]

extension-pkg-allow-list=OCP

[BASIC]

# Good variable names which should always be accepted, separated by a comma
good-names=i,j,k,u,v,x,y,z,ex,Run,_,X,Y,Z,XY,YZ,ZX,XZ,YX,ZY

disable=
    unsubscriptable-object,	# False positives
    use-a-generator,				# all([..]) is just fine
    protected-access,				# _variable to be hiddened from external users
    too-many-arguments,			# CAD is complex
    too-few-public-methods  # Objects and Operations will not have methods outside of _init

ignore-paths=
    ./src/build123d/_version.py # Generated

ignored-modules=OCP,vtkmodules,scipy.spatial,ezdxf,anytree,IPython,trianglesolver,scipy,numpy


================================================
FILE: .readthedocs.yaml
================================================
version: 2

formats:
  - epub
  - pdf

build:
  os: "ubuntu-22.04"
  tools:
    python: "3.10"
  apt_packages:
    - graphviz
  jobs:
    post_checkout:
      # necessary to ensure that the development builds get a correct version tag
      - git fetch --unshallow || true

# Build from the docs/ directory with Sphinx
sphinx:
  configuration: docs/conf.py

python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs



================================================
FILE: docs/advanced.rst
================================================
###############
Advanced Topics
###############

.. toctree::
    :maxdepth: 2

    algebra_performance.rst
    location_arithmetic.rst
    algebra_definition.rst
    center.rst
    debugging_logging.rst



================================================
FILE: docs/advantages.rst
================================================
As mentioned previously, the most significant advantage is that build123d is more pythonic.
Specifically:

Standard Python Context Manager
===============================

The creation of standard instance variables, looping and other normal python operations
is enabled by the replacement of method chaining (fluent programming) with a standard
python context manager.

.. code-block:: python

    # CadQuery Fluent API
    pillow_block = (cq.Workplane("XY")
        .box(height, width, thickness)
        .edges("|Z")
        .fillet(fillet)
        .faces(">Z")
        .workplane()
        ...
    )

.. code-block:: python

    # build123d API
    with BuildPart() as pillow_block:
        with BuildSketch() as plan:
            Rectangle(width, height)
            fillet(plan.vertices(), radius=fillet)
        extrude(thickness)
        ...

The use of the standard `with` block allows standard python instructions to be
inserted anyway in the code flow.  One can insert a CQ-editor `debug` or standard `print`
statement anywhere in the code without impacting functionality. Simple python
`for` loops can be used to repetitively create objects instead of forcing users
into using more complex `lambda` and `iter` operations.

Instantiated Objects
====================

Each object and operation is now a class instantiation that interacts with the
active context implicitly for the user. These instantiations can be assigned to
an instance variable as with standard python programming for direct use.

.. code-block:: python

    with BuildSketch() as plan:
        r = Rectangle(width, height)
        print(r.area)
        ...

Operators
=========

New operators have been created to extract information from objects created previously
in the code. The `@` operator extracts the position along an Edge or Wire while the
`%` operator extracts the tangent along an Edge or Wire. The position parameter are float
values between 0.0 and 1.0 which represent the beginning and end of the line. In the following
example, a spline is created from the end of l5 (`l5 @ 1`) to the beginning of l6 (`l6 @ 0`)
with tangents equal to the tangents of l5 and l6 at their end and beginning respectively.
Being able to extract information from existing features allows the user to "snap" new
features to these points without knowing their numeric values.

.. code-block:: python

    with BuildLine() as outline:
        ...
        l5 = Polyline(...)
        l6 = Polyline(...)
        Spline(l5 @ 1, l6 @ 0, tangents=(l5 % 1, l6 % 0))


Last Operation Objects
======================
All of the `vertices()`, `edges()`, `faces()`, and `solids()` methods of the builders
can either return all of the objects requested or just the objects changed during the
last operation. This allows the user to easily access features for further refinement,
as shown in the following code where the final line selects the edges that were added
by the last operation and fillets them. Such a selection would be quite difficult
otherwise.

.. literalinclude:: ../examples/intersecting_pipes.py
    :lines: 30, 39-49


Extensions
==========
Extending build123d is relatively simple in that custom objects or operations
can be created as new classes without the need to monkey patch any of the
core functionality. These new classes will be seen in IDEs which is not
possible with monkey patching the core CadQuery classes.

Enums
=====

All `Literal` strings have been replaced with `Enum` which allows IDEs to
prompt users for valid options without having to refer to documentation.

Selectors replaced by Lists
===========================
String based selectors have been replaced with standard python filters and
sorting which opens up the full functionality of python lists. To aid the
user, common operations have been optimized as shown here along with
a fully custom selection:

.. code-block:: python

    top = rail.faces().filter_by(Axis.Z)[-1]
    ...
    outside_vertices = filter(
        lambda v: (v.Y == 0.0 or v.Y == height) and -width / 2 < v.X < width / 2,
        din.vertices(),
    )



================================================
FILE: docs/algebra_definition.rst
================================================
.. _algebra_definition:

Algebraic definition
========================

Objects and arithmetic
------------------------

**Set definitions:**

:math:`C^3` is the set of all ``Part`` objects ``p`` with ``p._dim = 3``

:math:`C^2` is the set of all ``Sketch`` objects ``s`` with ``s._dim = 2``

:math:`C^1` is the set of all ``Curve`` objects ``c`` with ``c._dim = 1``

**Neutral elements:**

:math:`c^3_0` is the empty ``Part`` object ``p0 = Part()`` with ``p0._dim = 3`` and ``p0.wrapped = None``

:math:`c^2_0` is the empty ``Sketch`` object ``s0 = Sketch()`` with ``s0._dim = 2`` and ``s0.wrapped = None``

:math:`c^1_0` is the empty ``Curve`` object ``c0 = Curve()`` with ``c0._dim = 1`` and ``c0.wrapped = None``


**Sets of predefined basic shapes:**

:math:`B^3 := \lbrace` ``Part``, ``Box``, ``Cylinder``, ``Cone``, ``Sphere``, ``Torus``, ``Wedge``, ``Hole``, ``CounterBoreHole``, ``CounterSinkHole`` :math:`\rbrace`

:math:`B^2 := \lbrace` ``Sketch``, ``Rectangle``, ``Circle``, ``Ellipse``, ``Rectangle``, ``Polygon``, ``RegularPolygon``, ``Text``, ``Trapezoid``, ``SlotArc``, ``SlotCenterPoint``, ``SlotCenterToCenter``, ``SlotOverall`` :math:`\rbrace`

:math:`B^1 := \lbrace` ``Curve``, ``Bezier``, ``FilletPolyline``, ``PolarLine``, ``Polyline``, ``Spline``, ``Helix``, ``CenterArc``, ``EllipticalCenterArc``, ``RadiusArc``, ``SagittaArc``, ``TangentArc``, ``ThreePointArc``, ``JernArc`` :math:`\rbrace`

with :math:`B^3 \subset C^3, B^2 \subset C^2` and :math:`B^1 \subset C^1`


**Operations:**

:math:`+: C^n \times C^n \rightarrow C^n` with :math:`(a,b) \mapsto a + b`,  :math:`\;` for :math:`n=1,2,3`

    :math:`\; a + b :=` ``a.fuse(b)`` for each operation

:math:`-: C^n \rightarrow C^n` with :math:`a \mapsto -a`,  :math:`\;` for :math:`n=1,2,3`

    :math:`\; b + (-a) :=` ``b.cut(a)`` for each operation (implicit definition)


:math:`\&: C^n \times C^n \rightarrow C^n` with :math:`(a,b) \mapsto a \; \& \; b`,  :math:`\;` for :math:`n=2,3`

    :math:`\; a \; \& \; b :=` ``a.intersect(b)`` for each operation

    * :math:`\&` is not defined for :math:`n=1` in build123d
    * The following relationship holds: :math:`a \; \& \; b = (a + b) + -(a + (-b)) + -(b + (-a))`


**Abelian groups**

:math:`( C^n, \; c^n_0, \; +, \; -)` :math:`\;`  are abelian groups for :math:`n=1,2,3`.

* The implementation ``a - b = a.cut(b)`` needs to be read as :math:`a + (-b)` since the group does not have a binary ``-`` operation. As such, :math:`a - (b - c) = a + -(b + -c)) \ne a - b + c`
* This definition also includes that neither ``-`` nor ``&`` are commutative.


Locations, planes and location arithmetic
---------------------------------------------

**Set definitions:**

:math:`L  := \lbrace` ``Location((x, y, z), (a, b, c))`` :math:`: x,y,z \in R \land a,b,c \in R \rbrace\;`

    with :math:`a,b,c` being angles in degrees.

:math:`P  := \lbrace` ``Plane(o, x, z)`` :math:`: o,x,z ∈ R^3 \land \|x\| = \|z\| = 1\rbrace`

    with ``o`` being the origin and ``x``, ``z`` the x- and z-direction of the plane.

Neutral element: :math:`\; l_0 \in L`: ``Location()``

**Operations:**

:math:`*: L \times L \rightarrow L` with :math:`(l_1,l_2) \mapsto l_1 * l_2`

    :math:`\; l_1 * l_2 :=`  ``l1 * l2`` (multiply two locations)

:math:`*: P \times L \rightarrow P` with :math:`(p,l) \mapsto p * l`

    :math:`\; p * l :=` ``Plane(p.location * l)`` (move plane :math:`p \in P` to location :math:`l \in L`)

Inverse element: :math:`\; l^{-1} \in L`: ``l.inverse()``


**Placing objects onto planes**

:math:`*: P \times C^n  \rightarrow C^n \;`  with :math:`(p,c) \mapsto p * c`,  :math:`\;` for :math:`n=1,2,3`

    Locate an object :math:`c \in C^n` onto plane :math:`p \in P`, i.e. ``c.moved(p.location)``

**Placing objects at locations**

:math:`*: L \times C^n  \rightarrow C^n \;`  with :math:`(l,c) \mapsto l * c`,  :math:`\;` for :math:`n=1,2,3`

    Locate an object :math:`c \in C^n` at location :math:`l \in L`, i.e. ``c.moved(l)``



================================================
FILE: docs/algebra_performance.rst
================================================
.. _algebra_performance:

Performance considerations in algebra mode
===============================================

Creating lots of Shapes in a loop means for every step ``fuse`` and ``clean`` will be called. 
In an example like the below, both functions get slower and slower the more objects are 
already fused. Overall it takes on an M1 Mac 4.76 sec.

.. code-block:: python

    diam = 80
    holes = Sketch()
    r = Rectangle(2, 2)
    for loc in GridLocations(4, 4, 20, 20):
        if loc.position.X**2 + loc.position.Y**2 < (diam / 2 - 1.8) ** 2:
            holes += loc * r

    c = Circle(diam / 2) - holes


One way to avoid it is to use lazy evaluation for the algebra operations. Just collect all objects and 
then call ``fuse`` (``+``) once with all objects and ``clean`` once. Overall it takes 0.19 sec.

.. code-block:: python

    r = Rectangle(2, 2)
    holes = [
        loc * r
        for loc in GridLocations(4, 4, 20, 20).locations
        if loc.position.X**2 + loc.position.Y**2 < (diam / 2 - 1.8) ** 2
    ]

    c = Circle(diam / 2) - holes

Another way to leverage the vectorized algebra operations is to add a list comprehension of objects to
an empty ``Part``, ``Sketch`` or ``Curve``:

.. code-block:: python

    polygons = Sketch() + [
        loc * RegularPolygon(radius=5, side_count=5)
        for loc in GridLocations(40, 30, 2, 2)
    ]

This again ensures one single ``fuse`` and ``clean`` call.



================================================
FILE: docs/assemblies.rst
================================================
.. _assembly:

##########
Assemblies
##########

Most CAD designs consist of more than one part which are naturally arranged in
some type of assembly. Once parts have been assembled in a :class:`~topology.Compound` object
they can be treated as a unit - i.e. :meth:`~topology.Shape.moved` or exported.

To create an assembly in build123d, one needs to
create a tree of parts by simply assigning either a :class:`~topology.Compound` object's ``parent`` or
``children`` attributes. To illustrate the process, we'll extend the
:ref:`Joint Tutorial <joint_tutorial>`.

****************
Assigning Labels
****************

In order keep track of objects one can assign a ``label`` to all :class:`~topology.Shape` objects.
Here we'll assign labels to all of the components that will be part of the box
assembly:

.. literalinclude:: tutorial_joints.py
    :start-after: [Add labels]
    :end-before: [Create assembly]

The labels are just strings with no further limitations (they don't have to be unique
within the assembly).

****************************
Create the Assembly Compound
****************************

Creation of the assembly is done by simply creating a :class:`~topology.Compound` object and assigning
appropriate ``parent`` and ``children`` attributes as shown here:

.. literalinclude:: tutorial_joints.py
    :start-after: [Create assembly]
    :end-before: [Display assembly]

To display the topology of an assembly :class:`~topology.Compound`, the :meth:`~topology.Shape.show_topology`
method can be used as follows:

.. literalinclude:: tutorial_joints.py
    :start-after: [Display assembly]
    :end-before: [Add to the assembly by assigning the parent attribute of an object]

which results in:

.. code::

        assembly        Compound at 0x7fc8ee235760, Location(p=(0, 0, 0), o=(-0, 0, -0))
        ├── box         Compound at 0x7fc8ee2188b0, Location(p=(0, 0, 50), o=(-0, 0, -0))
        ├── lid         Compound at 0x7fc8ee228460, Location(p=(-26, 0, 181), o=(-180, 30, -0))
        ├── inner hinge Hinge    at 0x7fc9292c3f70, Location(p=(-119, 60, 122), o=(90, 0, -150))
        └── outer hinge Hinge    at 0x7fc9292c3f40, Location(p=(-150, 60, 50), o=(90, 0, 90))

To add to an assembly :class:`~topology.Compound` one can change either ``children`` or ``parent`` attributes.

.. literalinclude:: tutorial_joints.py
    :start-after: [Add to the assembly by assigning the parent attribute of an object]
    :end-before: [Check that the components in the assembly don't intersect]

and now the screw is part of the assembly.

.. code::

        assembly        Compound at 0x7fc8ee235760, Location(p=(0, 0, 0), o=(-0, 0, -0))
        ├── box         Compound at 0x7fc8ee2188b0, Location(p=(0, 0, 50), o=(-0, 0, -0))
        ├── lid         Compound at 0x7fc8ee228460, Location(p=(-26, 0, 181), o=(-180, 30, -0))
        ├── inner hinge Hinge    at 0x7fc9292c3f70, Location(p=(-119, 60, 122), o=(90, 0, -150))
        ├── outer hinge Hinge    at 0x7fc9292c3f40, Location(p=(-150, 60, 50), o=(90, 0, 90))
        └── M6 screw    Compound at 0x7fc8ee235310, Location(p=(-157, -40, 70), o=(-0, -90, -60))

.. _shallow_copy:

*********************************
Shallow vs. Deep Copies of Shapes
*********************************

Build123d supports the standard python ``copy`` module which provides two different types of
copy operations ``copy.copy()`` and ``copy.deepcopy()``.

Build123d's implementation of ``deepcopy()`` for the :class:`~topology.Shape` class (e.g. ``Solid``, ``Face``, etc.)
does just that, creates a complete copy of the original  all the way down to the CAD object.
``deepcopy`` is therefore suited to the case where the copy will be subsequently modified to
become its own unique item.

However, when building an assembly a common use case is to include many instances of an
object, each one identical but in a different location. This is where ``copy.copy()`` is
very useful as it copies all of the :class:`~topology.Shape` except for the actual CAD object
which instead is a reference to the original (OpenCascade refers this as a ``TShape``). As
it's a reference any changes to the original will be seen in all of the shallow copies.

Consider this example where 100 screws are added to an assembly:

.. image:: reference_assembly.svg
    :align: center

.. code::

    screw = import_step("M6-1x12-countersunk-screw.step")
    locs = HexLocations(6, 10, 10).local_locations

    screw_copies = [copy.deepcopy(screw).locate(loc) for loc in locs]
    copy_assembly = Compound(children=screw_copies)
    export_step(copy_assembly, "copy_assembly.step")

which takes about 5 seconds to run (on an older computer) and produces
a file of size 51938 KB. However, if a shallow copy is used instead:

.. code::

    screw = import_step("M6-1x12-countersunk-screw.step")
    locs = HexLocations(6, 10, 10).local_locations

    screw_references = [copy.copy(screw).locate(loc) for loc in locs]
    reference_assembly = Compound(children=screw_references)
    export_step(reference_assembly, "reference_assembly.step")

this takes about ¼ second and produces a file of size 550 KB - just over
1% of the size of the ``deepcopy()`` version and only 12% larger than the
screw's step file.

Using ``copy.copy()`` to create references to the original CAD object
for assemblies can substantially reduce the time and resources used
to create and store that assembly.

************************
Shapes are Anytree Nodes
************************

The build123d assembly constructs are built using the python
`anytree <https://anytree.readthedocs.io/en/latest/>`_ package by making the build123d
:class:`~topology.Shape` class a sub-class of anytree's ``NodeMixin`` class. Doing so
adds the following attributes to :class:`~topology.Shape`:

* ``parent`` - Parent Node. On set, the node is detached from any previous parent node and attached to the new node.
* ``children`` - Tuple of all child nodes.
* ``path`` - Path of this ``Node``.
* ``iter_path_reverse`` - Iterate up the tree from the current node.
* ``ancestors`` - All parent nodes and their parent nodes.
* ``descendants`` - All child nodes and all their child nodes.
* ``root`` - Tree Root Node.
* ``siblings`` - Tuple of nodes with the same parent.
* ``leaves`` - Tuple of all leaf nodes.
* ``is_leaf`` - ``Node`` has no children (External Node).
* ``is_root`` - ``Node`` is tree root.
* ``height`` - Number of edges on the longest path to a leaf ``Node``.
* ``depth`` - Number of edges to the root ``Node``.

.. note::

    Changing the ``children`` attribute

    Any iterator can be assigned to the ``children`` attribute but subsequently the children
    are stored as immutable ``tuple`` objects.  To add a child to an existing :class:`~topology.Compound`
    object, the ``children`` attribute will have to be reassigned.

    .. _pack:

************************
Iterating Over Compounds
************************

As Compounds are containers for shapes, build123d can iterate over these as required.
Complex nested assemblies (compounds within compounds) do not need to be looped over with recursive functions.
In the example below, the variable total_volume holds the sum of all the volumes in each solid in an assembly.
Compare this to assembly3_volume which only results in the volume of the top level part.

.. code:: python

    # [import]
    from build123d import *
    from ocp_vscode import *

    # Each assembly has a box and the previous assembly.
    assembly1 = Compound(label='Assembly1', children=[Box(1, 1, 1),])
    assembly2 = Compound(label='Assembly2', children=[assembly1, Box(1, 1, 1)])
    assembly3 = Compound(label='Assembly3', children=[assembly2, Box(1, 1, 1)])
    total_volume = sum(part.volume for part in assembly3.solids()) # 3
    assembly3_volume = assembly3.volume # 1 

******
pack
******

The  :meth:`pack.pack` function arranges objects in a compact, non-overlapping layout within a square(ish) 2D area. It is designed to minimize the space between objects while ensuring that no two objects overlap.

.. py:module:: pack


.. autofunction:: pack



Detailed Description
---------------------

The ``pack`` function uses a bin-packing algorithm to efficiently place objects within a 2D plane, ensuring that there is no overlap and that the space between objects is minimized. This is particularly useful in scenarios where spatial efficiency is crucial, such as layout design and object arrangement in constrained spaces.

The function begins by calculating the bounding boxes for each object, including the specified padding. It then uses a helper function ``_pack2d`` to determine the optimal positions for each object within the 2D plane. The positions are then translated back to the original objects, ensuring that they are arranged without overlapping.

Usage Note
----------

The ``align_z`` parameter is especially useful when creating print-plates for 3D printing. By aligning the bottoms of the shapes to the same XY plane, you ensure that the objects are perfectly positioned for slicing software, which will no longer need to perform this alignment for you. This can streamline the process and improve the accuracy of the print setup.

Example Usage
-------------

.. code:: python

    # [import]
    from build123d import *
    from ocp_vscode import *


    # [initial space]
    b1 = Box(100, 100, 100, align=(Align.CENTER, Align.CENTER, Align.MIN))
    b2 = Box(54, 54, 54, align=(Align.CENTER, Align.CENTER, Align.MAX), mode=Mode.SUBTRACT)
    b3 = Box(34, 34, 34, align=(Align.MIN, Align.MIN, Align.CENTER), mode=Mode.SUBTRACT)
    b4 = Box(24, 24, 24, align=(Align.MAX, Align.MAX, Align.CENTER), mode=Mode.SUBTRACT)



.. image:: assets/pack_demo_initial_state.svg
    :align: center


.. code:: python

    # [pack 2D]

    xy_pack = pack(
        [b1, b2, b3, b4],
        padding=5,
        align_z=False
    )


.. image:: assets/pack_demo_packed_xy.svg
    :align: center


.. code:: python

    # [Pack and align_z]

    z_pack = pack(
        [b1, b2, b3, b4],
        padding=5,
        align_z=True
    )

.. image:: assets/pack_demo_packed_z.svg
    :align: center


Tip
---

If you place the arranged objects into a ``Compound``, you can easily determine their bounding box and check whether the objects fit on your print bed.


.. code:: python

    # [bounding box]
    print(Compound(xy_pack).bounding_box())
    # bbox: 0.0 <= x <= 159.0, 0.0 <= y <= 129.0, -54.0 <= z <= 100.0
    
    print(Compound(z_pack).bounding_box())
    # bbox: 0.0 <= x <= 159.0, 0.0 <= y <= 129.0, 0.0 <= z <= 100.0



================================================
FILE: docs/build_line.rst
================================================
#########
BuildLine
#########

BuildLine is a python context manager that is used to create one dimensional
objects - objects with the property of length but not area - that are typically
used as part of a BuildSketch sketch or a BuildPart path.

The complete API for BuildLine is located at the end of this section.

*******************
Basic Functionality
*******************

The following is a simple BuildLine example:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 1]
    :end-before: [Ex. 1]

The ``with`` statement creates the ``BuildLine`` context manager with the
identifier ``example_1``. The objects and operations that are within the
scope (i.e. indented) of this context will contribute towards the object
being created by the context manager.  For ``BuildLine``, this object is
``line`` and it's referenced as ``example_1.line``.

The first object in this example is a ``Line`` object which is used to create
a straight line from coordinates (0,0) to (2,0) on the default XY plane.
The second object is a ``ThreePointArc`` that starts and ends at the two
ends of the line.

.. image:: assets/buildline_example_1.svg
    :align: center

***********
Constraints
***********

Building with constraints enables the designer to capture design intent and
add a high degree of robustness to their designs.  The following sections
describe creating positional and tangential constraints as well as using
object attributes to enable this type of design.

@ ``position_at`` Operator
===========================

In the previous example, the ``ThreePointArc`` started and ended at the
two ends of the ``Line`` but this was done by referring to the same
point ``(0,0)`` and ``(2,0)``.  This can be improved upon by specifying
constraints that lock the arc to those two end points, as follows:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 2]
    :end-before: [Ex. 2]

Here instance variables ``l1`` and ``l2`` are assigned to the two BuildLine
objects and the ``ThreePointArc`` references the beginning of the straight
line with ``l1 @ 0`` and the end with ``l1 @ 1``.  The ``@`` operator takes
a float (or integer) parameter between 0 and 1 and determines a position
at this fractional position along the line's length.

This example can be improved on further by calculating the mid-point
of the arc as follows:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 3]
    :end-before: [Ex. 3]

Here ``l1 @ 0.5`` finds the center of ``l1`` while ``l1 @ 0.5 + (0, 1)`` does
a vector addition to generate the point ``(1,1)``.

To make the design even more parametric, the height of the arc can be calculated
from ``l1`` as follows:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 4]
    :end-before: [Ex. 4]

The arc height is now calculated as ``(0, l1.length / 2)`` by using the ``length``
property of ``Edge`` and ``Wire`` shapes.  At this point the ``ThreePointArc`` is
fully parametric and able to generate the same shape for any horizontal line.

% ``tangent_at`` Operator
=========================

The other operator that is commonly used within BuildLine is ``%`` the tangent at
operator. Here is another example:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 5]
    :end-before: [Ex. 5]

which generates (note that the circles show line junctions):

.. image:: assets/buildline_example_5.svg
    :align: center

The ``JernArc`` has the following parameters:

* ``start=l2 @ 1`` - start the arc at the end of line ``l2``,
* ``tangent=l2 % 1`` - the tangent of the arc at the start point is equal to the ``l2``\'s,
  tangent at its end (shown as a dashed line)
* ``radius=0.5`` - the radius of the arc, and
* ``arc_size=90`` the angular size of the arc.

The final line starts at the end of ``l3`` and ends at a point calculated from the length
of ``l2`` and the radius of arc ``l3``.

Building with constraints as shown here will ensure that your designs both fully represent
design intent and are robust to design changes.

************************
BuildLine to BuildSketch
************************

As mentioned previously, one of the two primary reasons to create BuildLine objects is to
use them in BuildSketch.  When a BuildLine context manager exits and is within the scope of a
BuildSketch context manager it will transfer the generated line to BuildSketch. The BuildSketch
:meth:`~operations_sketch.make_face` or :meth:`~operations_sketch.make_hull`  operations are then used
to transform the line (specifically a list of Edges) into a Face - the native BuildSketch
objects.

Here is an example of using BuildLine to create an object that otherwise might be
difficult to create:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 6]
    :end-before: [Ex. 6]

which generates:

.. image:: assets/buildline_example_6.svg
    :align: center

.. note:: SVG import to BuildLine

    The BuildLine code used in this example was generated by translating a SVG file
    into BuildLine source code with the :func:`~importers.import_svg_as_buildline_code`
    function. For example:

    .. code::

        svg_code, builder_name = import_svg_as_buildline_code("club.svg")

    would translate the "club.svg" image file's paths into BuildLine code much like
    that shown above. From there it's easy for a user to add constraints or otherwise
    enhance the original image and use it in their design.

**********************
BuildLine to BuildPart
**********************

The other primary reasons to use BuildLine is to create paths for BuildPart
:meth:`~operations_generic.sweep` operations. Here some curved and straight segments
define a path:

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 7]
    :end-before: [Ex. 7]

which generates:

.. image:: assets/buildline_example_7.svg
    :align: center

There are few things to note from this example:

* The @ and % operators are used to create a plane normal to the beginning of the
  path with which to create the circular section used by the sweep operation
  (this plane is not one of the ordinal planes).
* Both the path generated by BuildLine and the section generated by BuildSketch
  have been transferred to BuildPart when each of them exit.
* The BuildPart ``Sweep`` operation is using the path and section previously
  transferred to it (as "pending" objects) as parameters of the sweep. The
  ``Sweep`` operation "consumes" these pending objects as to not interfere with
  subsequence operations.

***********************
Working on other Planes
***********************

So far all of the examples were created on ``Plane.XY`` - the default plane - which is equivalent
to global coordinates. Sometimes it's convenient to work on another plane, especially when
creating paths for BuildPart ``Sweep`` operations.

.. literalinclude:: objects_1d.py
    :start-after: [Ex. 8]
    :end-before: [Ex. 8]

which generates:

.. image:: assets/buildline_example_8.svg
    :align: center

Here the BuildLine object is created on ``Plane.YZ`` just by specifying the working plane
during BuildLine initialization.

There are three rules to keep in mind when working with alternate planes in BuildLine:

#. ``BuildLine`` accepts a single ``Plane`` to work with as opposed to other Builders
   that accept more than one workplane.
#. Values entered as tuples such as ``(1, 2)`` or ``(1, 2, 3)`` will be localized to the
   current workplane.  This rule applies to points and to the use of tuples to modify
   locations calculated with the ``@`` and ``%`` operators such as ``l1 @ 1 + (1, 1)``.
   For example, if the workplane is ``Plane.YZ`` the local value of ``(1, 2)`` would
   be converted to ``(0, 1, 2)`` in global coordinates.  Three tuples are converted as
   well - ``(1, 2, 3)`` on ``Plane.YZ`` would be ``(3, 1, 2)`` in global coordinates.
   Providing values in local coordinates allows the designer to automate such
   conversions.
#. Values entered using the ``Vector`` class or those generated by the ``@`` operator
   are considered global values and are not localized.  For example:
   ``Line(Vector(1, 2, 3), Vector(4, 5, 6))`` will generate the same line independent
   of the current workplane. It's unlikely that users will need to use ``Vector``
   values but the option is there.

Finally, BuildLine's workplane need not be one of the predefined ordinal planes, it
could be one created from a surface of a BuildPart part that is currently under
construction.

*********
Reference
*********
.. py:module:: build_line

.. autoclass:: BuildLine
    :members:



================================================
FILE: docs/build_part.rst
================================================
#########
BuildPart
#########

BuildPart is a python context manager that is used to create three dimensional
objects - objects with the property of volume - that are typically
finished parts.

The complete API for BuildPart is located at the end of this section.

*******************
Basic Functionality
*******************

The following is a simple BuildPart example:

.. literalinclude:: general_examples.py
    :start-after: [Ex. 2]
    :end-before: [Ex. 2]

The ``with`` statement creates the ``BuildPart`` context manager with the
identifier ``ex2`` (this code is the second of the introductory examples).
The objects and operations that are within the
scope (i.e. indented) of this context will contribute towards the object
being created by the context manager.  For ``BuildPart``, this object is
``part`` and it's referenced as ``ex2.part``.

The first object in this example is a ``Box`` object which is used to create
a polyhedron with rectangular faces centered on the default ``Plane.XY``.
The second object is a ``Cylinder`` that is subtracted from the box as directed
by the ``mode=Mode.SUBTRACT`` parameter thus creating a hole.

.. image:: assets/general_ex2.svg
    :align: center

*******************
Implicit Parameters
*******************

The BuildPart context keeps track of pending objects such that they can be used
implicitly - there are a couple things to consider when deciding how to proceed:

* For sketches, the planes that they were constructed on is maintained in internal
  data structures such that operations like :func:`~operations_part.extrude` will
  have a good reference for the extrude direction.  One can pass a Face to extrude
  but it will then be forced to use the normal direction at the center of the Face
  as the extrude direction which unfortunately can be reversed in some circumstances.
* Implicit parameters save some typing but hide some functionality - users have
  to decide what works best for them.

This tea cup example uses implicit parameters - note the :func:`~operations_generic.sweep`
operation on the last line:

.. literalinclude:: ../examples/tea_cup.py
    :start-after: [Code]
    :end-before: [End]
    :emphasize-lines: 52

:func:`~operations_generic.sweep` requires a 2D cross section - ``handle_cross_section`` -
and a path - ``handle_path`` - which are both passed implicitly.

.. image:: tea_cup.png
  :align: center

*****
Units
*****

Parts created with build123d have no inherent units associated with them. However, when
exporting parts to external formats like ``STL`` or ``STEP`` the units are assumed to
be millimeters (mm).  To be more explicit with units one can use the technique shown
in the above tea cup example where linear dimensions are followed by ``* MM`` which
multiplies the dimension by the ``MM`` scaling factor - in this case ``1``.

The following dimensional constants are pre-defined:

.. code:: python

    MM = 1
    CM = 10 * MM
    M = 1000 * MM
    IN = 25.4 * MM
    FT = 12 * IN
    THOU = IN / 1000

Some export formats like DXF have the ability to explicitly set the units used.

*********
Reference
*********

.. py:module:: build_part

.. autoclass:: BuildPart
    :members:



================================================
FILE: docs/build_sketch.rst
================================================
###########
BuildSketch
###########

BuildSketch is a python context manager that is used to create planar two dimensional
objects - objects with the property of area but not volume - that are typically
used as profiles for BuildPart operations like :func:`~operations_part.extrude` or
:func:`~operations_part.revolve`.

The complete API for BuildSketch is located at the end of this section.

*******************
Basic Functionality
*******************

The following is a simple BuildSketch example:

.. literalinclude:: objects_2d.py
    :start-after: [Ex. 13]
    :end-before: [Ex. 13]

The ``with`` statement creates the ``BuildSketch`` context manager with the
identifier ``circle_with_hole``. The objects and operations that are within the
scope (i.e. indented) of this context will contribute towards the object
being created by the context manager.  For ``BuildSketch``, this object is
``sketch`` and it's referenced as ``circle_with_hole.sketch``.

The first object in this example is a ``Circle`` object which is used to create
a filled circular shape on the default XY plane. The second object is a ``Rectangle``
that is subtracted from the circle as directed by the ``mode=Mode.SUBTRACT`` parameter.
A key aspect of sketch objects is that they are all filled shapes and not just
a shape perimeter which enables combining subsequent shapes with different modes
(the valid values of Mode are ``ADD``, ``SUBTRACT``, ``INTERSECT``, ``REPLACE``,
and ``PRIVATE``).

.. image:: assets/circle_with_hole.svg
    :align: center

.. _sketching_on_other_planes:

*************************
Sketching on other Planes
*************************

Often when designing parts one needs to build on top of other features.  To facilitate
doing this ``BuildSketch`` allows one to create sketches on any Plane while allowing
the designer to work in a local X, Y coordinate system. It might be helpful to think
of what is happening with this metaphor:

#. When instantiating ``BuildSketch`` one or more workplanes can be passed as parameters.
   These are the placement targets for the completed sketch.
#. The designer draws on a flat "drafting table" which is ``Plane.XY``.
#. Once the sketch is complete, it's applied like a sticker to all of the workplanes
   passed in step 1.

As an example, let's build the following simple control box with a display on an angled plane:

.. image:: assets/controller.svg
    :align: center

Here is the code:

.. literalinclude:: objects_2d.py
    :start-after: [Ex. 14]
    :end-before: [Ex. 14]
    :emphasize-lines: 14-25

The highlighted part of the code shows how a face is extracted from the design,
a workplane is constructed from this face and finally this workplane is passed
to ``BuildSketch`` as the target for the complete sketch.  Notice how the
``display`` sketch uses local coordinates for its features thus avoiding having
the user to determine how to move and rotate the sketch to get it where it
should go.

Note that ``BuildSketch`` accepts a sequence planes, faces and locations for
workplanes so creation of an explicit workplane is often not required. Being
able to work on multiple workplanes at once allows for features to be created
on multiple side of an object - say both the top and bottom - which is convenient
for symmetric parts.

*************************
Local vs. Global Sketches
*************************

In the above example the target for the sketch was not ``Plane.XY`` but a workplane
passed by the user.  Internally ``BuildSketch`` is always creating the sketch
on ``Plane.XY`` which one can see by looking at the ``sketch_local`` property of your
sketch.  For example, to display the local version of the ``display`` sketch from
above, one would use:

.. code-block:: python

    show_object(display.sketch_local, name="sketch on Plane.XY")

while the sketches as applied to their target workplanes is accessible through
the ``sketch`` property, as follows:

.. code-block:: python

    show_object(display.sketch, name="sketch on target workplane(s)")

When using the :func:`~operations_generic.add` operation to add an external Face
to a sketch the face will automatically be reoriented to ``Plane.XY`` before being
combined with the sketch.  As Faces don't provide an x-direction it's possible
that the new Face may not be oriented as expected. To reorient the Face manually
to ``Plane.XY`` one can use the :meth:`~geometry.to_local_coords` method as
follows:

.. code-block:: python

    reoriented_face = plane.to_local_coords(face)

where ``plane`` is the plane that ``face`` was constructed on.

*****************
Locating Features
*****************

Within a sketch features are positioned with ``Locations`` contexts
(see :ref:`Location Context <location_context_link>`) on the current workplane(s). The following
location contexts are available within a sketch:

* :class:`~build_common.GridLocations` : a X/Y grid of locations
* :class:`~build_common.HexLocations` : a hex grid of locations ideal for nesting circles
* :class:`~build_common.Locations` : a sequence of arbitrary locations
* :class:`~build_common.PolarLocations` : locations defined by radius and angle

Generally one would specify tuples of (X, Y) values when defining locations but
there are many options available to the user.


*********
Reference
*********

.. py:module:: build_sketch

.. autoclass:: BuildSketch
    :members:



================================================
FILE: docs/builder_api_reference.rst
================================================
.. _builder_api_reference:

############################
Builder Common API Reference
############################

The following are common to all the builders.

****************
Selector Methods
****************

.. automethod:: build_common::Builder.vertices
.. automethod:: build_common::Builder.faces
.. automethod:: build_common::Builder.edges
.. automethod:: build_common::Builder.wires
.. automethod:: build_common::Builder.solids

*****
Enums
*****

.. py:module:: build_enums

.. autoclass:: Align
.. autoclass:: CenterOf
.. autoclass:: FontStyle
.. autoclass:: GeomType
.. autoclass:: Keep
.. autoclass:: Kind
.. autoclass:: Mode
.. autoclass:: Select
.. autoclass:: SortBy
.. autoclass:: Transition
.. autoclass:: Until

*********
Locations
*********

.. autoclass:: build_common::Locations
.. autoclass:: build_common::GridLocations
.. autoclass:: build_common::HexLocations
.. autoclass:: build_common::PolarLocations



================================================
FILE: docs/builders.rst
================================================
########
Builders
########

The following sections describe each of the build123d stateful context builders.

.. toctree::
    :maxdepth: 2

    build_line.rst
    build_sketch.rst
    build_part.rst



================================================
FILE: docs/center.py
================================================
from build123d import *
from ocp_vscode import *

size = 50
#
# Symbols
#
bbox_symbol = Rectangle(4, 4)
geom_symbol = RegularPolygon(2, 3)
mass_symbol = Circle(2)

#
# 2D Center Options
#
triangle = RegularPolygon(size / 1.866, 3, rotation=90)
svg = ExportSVG(margin=5)
svg.add_layer("bbox", line_type=LineType.DASHED)
svg.add_shape(bounding_box(triangle), "bbox")
svg.add_shape(triangle)
svg.add_shape(bbox_symbol.located(Location(triangle.center(CenterOf.BOUNDING_BOX))))
svg.add_shape(mass_symbol.located(Location(triangle.center(CenterOf.MASS))))
svg.write("assets/center.svg")

#
# 1D Center Options
#
line = TangentArc((0, 0), (size, size), tangent=(1, 0))
svg = ExportSVG(margin=5)
svg.add_layer("bbox", line_type=LineType.DASHED)
svg.add_shape(line)
svg.add_shape(Polyline((0, 0), (size, 0), (size, size), (0, size), (0, 0)), "bbox")
svg.add_shape(bbox_symbol.located(Location(line.center(CenterOf.BOUNDING_BOX))))
svg.add_shape(mass_symbol.located(Location(line.center(CenterOf.MASS))))
svg.add_shape(geom_symbol.located(Location(line.center(CenterOf.GEOMETRY))))
svg.write("assets/one_d_center.svg")



================================================
FILE: docs/center.rst
================================================
##################
CAD Object Centers
##################

Finding the center of a CAD object is a surprisingly complex operation.  To illustrate
let's consider two examples: a simple isosceles triangle and a curved line (their bounding
boxes are shown with dashed lines):

.. image:: assets/center.svg
    :width: 49%

.. image:: assets/one_d_center.svg
    :width: 49%


One can see that there is are significant differences between the different types of 
centers. To allow the designer to choose the center that makes the most sense for the given
shape there are three possible values for the :class:`~build_enums.CenterOf` Enum:

==============================  ======  == == == ========
:class:`~build_enums.CenterOf`  Symbol  1D 2D 3D Compound
==============================  ======  == == == ========
CenterOf.BOUNDING_BOX           □       ✓  ✓  ✓  ✓
CenterOf.GEOMETRY               △       ✓  ✓       
CenterOf.MASS                   ○       ✓  ✓  ✓  ✓
==============================  ======  == == == ========



================================================
FILE: docs/cheat_sheet.rst
================================================
.. _cheat_sheet:

###########
Cheat Sheet
###########

.. card:: Stateful Contexts

    | :class:`~build_line.BuildLine` :class:`~build_part.BuildPart` :class:`~build_sketch.BuildSketch`
    | :class:`~build_common.GridLocations` :class:`~build_common.HexLocations` :class:`~build_common.Locations` :class:`~build_common.PolarLocations`

.. card:: Objects

    .. grid:: 3

        .. grid-item-card:: 1D - BuildLine

            | :class:`~objects_curve.Airfoil`
            | :class:`~objects_curve.ArcArcTangentArc`
            | :class:`~objects_curve.ArcArcTangentLine`
            | :class:`~objects_curve.Bezier`
            | :class:`~objects_curve.BlendCurve`
            | :class:`~objects_curve.CenterArc`
            | :class:`~objects_curve.DoubleTangentArc`
            | :class:`~objects_curve.EllipticalCenterArc`
            | :class:`~objects_curve.FilletPolyline`
            | :class:`~objects_curve.Helix`
            | :class:`~objects_curve.IntersectingLine`
            | :class:`~objects_curve.JernArc`
            | :class:`~objects_curve.Line`
            | :class:`~objects_curve.PointArcTangentArc`
            | :class:`~objects_curve.PointArcTangentLine`
            | :class:`~objects_curve.PolarLine`
            | :class:`~objects_curve.Polyline`
            | :class:`~objects_curve.RadiusArc`
            | :class:`~objects_curve.SagittaArc`
            | :class:`~objects_curve.Spline`
            | :class:`~objects_curve.TangentArc`
            | :class:`~objects_curve.ThreePointArc`

        .. grid-item-card:: 2D - BuildSketch

            | :class:`~drafting.Arrow`
            | :class:`~drafting.ArrowHead`
            | :class:`~objects_sketch.Circle`
            | :class:`~drafting.DimensionLine`
            | :class:`~objects_sketch.Ellipse`
            | :class:`~drafting.ExtensionLine`
            | :class:`~objects_sketch.Polygon`
            | :class:`~objects_sketch.Rectangle`
            | :class:`~objects_sketch.RectangleRounded`
            | :class:`~objects_sketch.RegularPolygon`
            | :class:`~objects_sketch.SlotArc`
            | :class:`~objects_sketch.SlotCenterPoint`
            | :class:`~objects_sketch.SlotCenterToCenter`
            | :class:`~objects_sketch.SlotOverall`
            | :class:`~objects_sketch.Text`
            | :class:`~drafting.TechnicalDrawing`
            | :class:`~objects_sketch.Trapezoid`
            | :class:`~objects_sketch.Triangle`

        .. grid-item-card:: 3D - BuildPart

            | :class:`~objects_part.Box`
            | :class:`~objects_part.Cone`
            | :class:`~objects_part.CounterBoreHole`
            | :class:`~objects_part.CounterSinkHole`
            | :class:`~objects_part.Cylinder`
            | :class:`~objects_part.Hole`
            | :class:`~objects_part.Sphere`
            | :class:`~objects_part.Torus`
            | :class:`~objects_part.Wedge`

.. card:: Operations

    .. grid:: 3

        .. grid-item-card:: 1D - BuildLine

            | :func:`~operations_generic.add`
            | :func:`~operations_generic.bounding_box`
            | :func:`~operations_generic.mirror`
            | :func:`~operations_generic.offset`
            | :func:`~operations_generic.project`
            | :func:`~operations_generic.scale`
            | :func:`~operations_generic.split`

        .. grid-item-card:: 2D - BuildSketch

            | :func:`~operations_generic.add`
            | :func:`~operations_generic.chamfer`
            | :func:`~operations_generic.fillet`
            | :func:`~operations_sketch.full_round`
            | :func:`~operations_sketch.make_face`
            | :func:`~operations_sketch.make_hull`
            | :func:`~operations_generic.mirror`
            | :func:`~operations_generic.offset`
            | :func:`~operations_generic.project`
            | :func:`~operations_generic.scale`
            | :func:`~operations_generic.split`
            | :func:`~operations_generic.sweep`
            | :func:`~operations_sketch.trace`

        .. grid-item-card:: 3D - BuildPart

            | :func:`~operations_generic.add`
            | :func:`~operations_generic.chamfer`
            | :func:`~operations_part.draft`
            | :func:`~operations_part.extrude`
            | :func:`~operations_generic.fillet`
            | :func:`~operations_part.loft`
            | :func:`~operations_part.make_brake_formed`
            | :func:`~operations_generic.mirror`
            | :func:`~operations_generic.offset`
            | :func:`~operations_generic.project`
            | :func:`~operations_part.revolve`
            | :func:`~operations_generic.scale`
            | :func:`~operations_part.section`
            | :func:`~operations_generic.split`
            | :func:`~operations_generic.sweep`

.. card:: Selectors

    .. grid:: 3

        .. grid-item-card:: 1D - BuildLine

            | :meth:`~build_common.Builder.vertices`
            | :meth:`~build_common.Builder.edges`
            | :meth:`~build_common.Builder.wires`

        .. grid-item-card:: 2D - BuildSketch

            | :meth:`~build_common.Builder.vertices`
            | :meth:`~build_common.Builder.edges`
            | :meth:`~build_common.Builder.wires`
            | :meth:`~build_common.Builder.faces`

        .. grid-item-card:: 3D - BuildPart

            | :meth:`~build_common.Builder.vertices`
            | :meth:`~build_common.Builder.edges`
            | :meth:`~build_common.Builder.wires`
            | :meth:`~build_common.Builder.faces`
            | :meth:`~build_common.Builder.solids`

.. card:: Selector Operators

    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | Operator | Operand                                                                                                 | Method                                         |
    +==========+=========================================================================================================+================================================+
    | >        | :class:`~geometry.Axis`, :class:`~topology.Edge`, :class:`~topology.Wire`, :class:`~build_enums.SortBy` | :meth:`~topology.ShapeList.sort_by`            |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | <        | :class:`~geometry.Axis`, :class:`~topology.Edge`, :class:`~topology.Wire`, :class:`~build_enums.SortBy` | :meth:`~topology.ShapeList.sort_by`            |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | >>       | :class:`~geometry.Axis`, :class:`~topology.Edge`, :class:`~topology.Wire`, :class:`~build_enums.SortBy` | :meth:`~topology.ShapeList.group_by`\[-1\]     |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | <<       | :class:`~geometry.Axis`, :class:`~topology.Edge`, :class:`~topology.Wire`, :class:`~build_enums.SortBy` | :meth:`~topology.ShapeList.group_by`\[0\]      |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | \|       | :class:`~geometry.Axis`, :class:`~geometry.Plane`, :class:`~build_enums.GeomType`                       | :meth:`~topology.ShapeList.filter_by`          |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | []       |                                                                                                         | python indexing / slicing                      |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+
    |          | :class:`~geometry.Axis`                                                                                 | :meth:`~topology.ShapeList.filter_by_position` |
    +----------+---------------------------------------------------------------------------------------------------------+------------------------------------------------+

.. card:: Edge and Wire Operators

    +----------+---------------------+-----------------------------------------+---------------------------------+
    | Operator | Operand             | Method                                  | Description                     |
    +==========+=====================+=========================================+=================================+
    | @        | 0.0 <= float <= 1.0 | :meth:`~topology.Mixin1D.position_at`   | Position as Vector along object |
    +----------+---------------------+-----------------------------------------+---------------------------------+
    | %        | 0.0 <= float <= 1.0 | :meth:`~topology.Mixin1D.tangent_at`    | Tangent as Vector along object  |
    +----------+---------------------+-----------------------------------------+---------------------------------+
    | ^        | 0.0 <= float <= 1.0 | :meth:`~topology.Mixin1D.location_at`   | Location along object           |
    +----------+---------------------+-----------------------------------------+---------------------------------+

.. card:: Shape Operators

    +----------+---------------------+-----------------------------------------+---------------------------------------------+
    | Operator | Operand             | Method                                  | Description                                 |
    +==========+=====================+=========================================+=============================================+
    | ==       | Any                 | :meth:`~topology.Shape.is_same`         | Compare CAD objects not including meta data |
    +----------+---------------------+-----------------------------------------+---------------------------------------------+

.. card:: Plane Operators

    +----------+----------------------------+-----------------------------+
    | Operator | Operand                    | Description                 |
    +==========+============================+=============================+
    | ==       | :class:`~geometry.Plane`   | Check for equality          |
    +----------+----------------------------+-----------------------------+
    | !=       | :class:`~geometry.Plane`   | Check for inequality        |
    +----------+----------------------------+-----------------------------+
    | \-       | :class:`~geometry.Plane`   | Reverse direction of normal |
    +----------+----------------------------+-----------------------------+
    | \*       | :class:`~geometry.Plane`   | Relocate by Location        |
    +----------+----------------------------+-----------------------------+

.. card:: Vector Operators

    +----------+------------------------------+-------------------------------------+---------------------+
    | Operator | Operand                      | Method                              | Description         |
    +==========+==============================+=====================================+=====================+
    | \+       | :class:`~geometry.Vector`    | :meth:`~geometry.Vector.add`        | add                 |
    +----------+------------------------------+-------------------------------------+---------------------+
    | \-       | :class:`~geometry.Vector`    | :meth:`~geometry.Vector.sub`        | subtract            |
    +----------+------------------------------+-------------------------------------+---------------------+
    | \*       | ``float``                    | :meth:`~geometry.Vector.multiply`   | multiply by scalar  |
    +----------+------------------------------+-------------------------------------+---------------------+
    | \/       | ``float``                    | :meth:`~geometry.Vector.multiply`   | divide by scalar    |
    +----------+------------------------------+-------------------------------------+---------------------+

.. card:: Vertex Operators

    +----------+-----------------------------+-------------------------------------+
    | Operator | Operand                     | Method                              |
    +==========+=============================+=====================================+
    | \+       | :class:`~topology.Vertex`   | :meth:`~topology.Vertex.add`        |
    +----------+-----------------------------+-------------------------------------+
    | \-       | :class:`~topology.Vertex`   | :meth:`~topology.Vertex.sub`        |
    +----------+-----------------------------+-------------------------------------+

.. card:: Enums

    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Align`            | MIN, CENTER, MAX                                                                                                                        |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.ApproxOption`     | ARC, NONE, SPLINE                                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.AngularDirection` | CLOCKWISE, COUNTER_CLOCKWISE                                                                                                            |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.CenterOf`         | GEOMETRY, MASS, BOUNDING_BOX                                                                                                            |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Extrinsic`        | XYZ, XZY, YZX, YXZ, ZXY, ZYX, XYX, XZX, YZY, YXY, ZXZ, ZYZ                                                                              |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.FontStyle`        | REGULAR, BOLD, BOLDITALIC, ITALIC                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.FrameMethod`      | CORRECTED, FRENET                                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.GeomType`         | BEZIER, BSPLINE, CIRCLE, CONE, CYLINDER, ELLIPSE, EXTRUSION, HYPERBOLA, LINE, OFFSET, OTHER, PARABOLA, PLANE, REVOLUTION, SPHERE, TORUS |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Intrinsic`        | XYZ, XZY, YZX, YXZ, ZXY, ZYX, XYX, XZX, YZY, YXY, ZXZ, ZYZ                                                                              |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.HeadType`         | CURVED, FILLETED, STRAIGHT                                                                                                              |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Keep`             | ALL, TOP, BOTTOM, BOTH, INSIDE, OUTSIDE                                                                                                 |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Kind`             | ARC, INTERSECTION, TANGENT                                                                                                              |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.LengthMode`       | DIAGONAL, HORIZONTAL, VERTICAL                                                                                                          |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.MeshType`         | OTHER, MODEL, SUPPORT, SOLIDSUPPORT                                                                                                     |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Mode`             | ADD, SUBTRACT, INTERSECT, REPLACE, PRIVATE                                                                                              |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.NumberDisplay`    | DECIMAL, FRACTION                                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.PageSize`         | A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, LEDGER, LEGAL, LETTER                                                                      |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.PositionMode`     | LENGTH, PARAMETER                                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.PrecisionMode`    | LEAST, AVERAGE, GREATEST, SESSION                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Select`           | ALL, LAST, NEW                                                                                                                          |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Side`             | BOTH, LEFT, RIGHT                                                                                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.SortBy`           | LENGTH, RADIUS, AREA, VOLUME, DISTANCE                                                                                                  |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.TextAlign`        | BOTTOM, CENTER, LEFT, RIGHT, TOP, TOPFIRSTLINE                                                                                          |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Transition`       | RIGHT, ROUND, TRANSFORMED                                                                                                               |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Unit`             | MC, MM, CM, M, IN, FT                                                                                                                   |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | :class:`~build_enums.Until`            | FIRST, LAST, NEXT, PREVIOUS                                                                                                             |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+



================================================
FILE: docs/conf.py
================================================
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import build123d

build123d_path = os.path.dirname(os.path.abspath(os.getcwd()))
source_files_path = os.path.join(build123d_path, "src", "build123d")
sys.path.insert(0, source_files_path)
sys.path.append(os.path.abspath("sphinxext"))
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

# -- Project information -----------------------------------------------------

project = "build123d"
copyright = "2022, Gumyr"
author = "Gumyr"

# The full version, including alpha/beta/rc tags
# version = build123d.__version__
release = build123d.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    #    "sphinx_autodoc_typehints",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_copybutton",
    "hoverxref.extension",
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None

autodoc_typehints = ["signature"]
# autodoc_typehints = ["description"]
# autodoc_typehints = ["both"]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "member-order": "alphabetical",
    "show-inheriance": False,
}

# autodoc_mock_imports = ["OCP"]

# Sphinx settings
add_module_names = False
python_use_unqualified_type_names = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for hoverxref -------------------------------------------------
hoverxref_role_types = {
    "hoverxref": "tooltip",
    "ref": "tooltip",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "mod": "tooltip",  # for Python Sphinx Domain
    "class": "tooltip",  # for Python Sphinx Domain
    "meth": "tooltip",  # for Python Sphinx Domain
    "func": "tooltip",  # for Python Sphinx Domain
}

hoverxref_roles = [
    "class",
    "meth",
]

hoverxref_domains = [
    "py",
]

html_logo = "assets/build123d_logo/logo.svg"



================================================
FILE: docs/debugging_logging.rst
================================================
###################
Debugging & Logging
###################

Debugging problems with your build123d design involves the same techniques
one would use to debug any Python source code; however, there are some
specific techniques that might be of assistance.  The following sections
describe these techniques.

***************
Python Debugger
***************

Many Python IDEs have step by step debugging systems that can be used to
walk through your code monitoring its operation with full visibility
of all Python objects.  Here is a screenshot of the Visual Studio Code
debugger in action:

.. image:: assets/VSC_debugger.png
    :align: center

This shows that a break-point has been encountered and the code operation
has been stopped.  From here all of the Python variables are visible and
the system is waiting on input from the user on how to proceed.  One can
enter the code that assigns ``top_face`` by pressing the down arrow button
on the top right. Following code execution like this is a very powerful
debug technique.

*******
Logging
*******

Build123d support standard python logging and generates its own log stream.
If one is using **cq-editor** as a display system there is a built in
``Log viewer`` tab that shows the current log stream - here is an example
of a log stream:

.. code-block:: bash

    [18:43:44.678646] INFO: Entering BuildPart with mode=Mode.ADD which is in different scope as parent
    [18:43:44.679233] INFO: WorkplaneList is pushing 1 workplanes: [Plane(o=(0.00, 0.00, 0.00), x=(1.00, 0.00, 0.00), z=(0.00, 0.00, 1.00))]
    [18:43:44.679888] INFO: LocationList is pushing 1 points: [(p=(0.00, 0.00, 0.00), o=(-0.00, 0.00, -0.00))]
    [18:43:44.681751] INFO: BuildPart context requested by Box
    [18:43:44.685950] INFO: Completed integrating 1 object(s) into part with Mode=Mode.ADD
    [18:43:44.690072] INFO: GridLocations is pushing 4 points: [(p=(-30.00, -20.00, 0.00), o=(-0.00, 0.00, -0.00)), (p=(-30.00, 20.00, 0.00), o=(-0.00, 0.00, -0.00)), (p=(30.00, -20.00, 0.00), o=(-0.00, 0.00, -0.00)), (p=(30.00, 20.00, 0.00), o=(-0.00, 0.00, -0.00))]
    [18:43:44.691604] INFO: BuildPart context requested by Hole
    [18:43:44.724628] INFO: Completed integrating 4 object(s) into part with Mode=Mode.SUBTRACT
    [18:43:44.728681] INFO: GridLocations is popping 4 points
    [18:43:44.747358] INFO: BuildPart context requested by chamfer
    [18:43:44.762429] INFO: Completed integrating 1 object(s) into part with Mode=Mode.REPLACE
    [18:43:44.765380] INFO: LocationList is popping 1 points
    [18:43:44.766106] INFO: WorkplaneList is popping 1 workplanes
    [18:43:44.766729] INFO: Exiting BuildPart

The build123d logger is defined by:

.. code-block:: python

    logging.getLogger("build123d").addHandler(logging.NullHandler())
    logger = logging.getLogger("build123d")

To export logs to a file, the following configuration is recommended:

.. code-block:: python

    logging.basicConfig(
        filename="myapp.log",
        level=logging.INFO,
        format="%(name)s-%(levelname)s %(asctime)s - [%(filename)s:%(lineno)s - \
        %(funcName)20s() ] - %(message)s",
    )

Logs can be easily placed in your code - here is an example:

.. code-block:: python

    logger.info("Exiting %s", type(self).__name__)


********
Printing
********

Sometimes the best debugging aid is just placing a print statement in your code. Many
of the build123d classes are setup to provide useful information beyond their class and
location in memory, as follows:

.. code-block:: python

    plane = Plane.XY.offset(1)
    print(f"{plane=}")

.. code-block:: bash

    plane=Plane(o=(0.00, 0.00, 1.00), x=(1.00, 0.00, 0.00), z=(0.00, 0.00, 1.00))

which shows the origin, x direction, and z direction of the plane.



================================================
FILE: docs/direct_api_reference.rst
================================================

####################
Direct API Reference
####################

The Direct API is an interface layer between the primary user interface API
(the Builders) and the OpenCascade (OCCT) API. This API is based on the CadQuery
Direct API (thank you to all of the CadQuery contributors that made this possible)
with the following major changes:

* PEP8 compliance
* New Axis class
* New ShapeList class enabling sorting and filtering of shape objects
* Literal strings replaced with Enums

*****************
Geometric Objects
*****************
The geometric classes defined by build123d are defined below. This parameters to the
CAD objects described in the following section are frequently of these types.

.. inheritance-diagram:: geometry
   :parts: 1

.. py:module:: geometry

.. autoclass:: Axis
   :special-members: __copy__,__deepcopy__, __neg__
.. autoclass:: BoundBox
.. autoclass:: Color
   :special-members: __copy__,__deepcopy__
.. autoclass:: Location
   :special-members: __copy__,__deepcopy__, __mul__, __pow__, __eq__, __neg__
.. autoclass:: LocationEncoder
.. autoclass:: Pos
.. autoclass:: Rot
.. autoclass:: Matrix
   :special-members: __copy__,__deepcopy__
.. autoclass:: Plane
   :special-members: __copy__,__deepcopy__, __eq__, __ne__, __neg__, __mul__
.. autoclass:: Rotation
.. autoclass:: Vector
   :special-members: __add__, __sub__, __mul__, __truediv__, __rmul__, __neg__, __abs__, __eq__, __copy__, __deepcopy__

*******************
Topological Objects
*******************
The topological object classes defined by build123d are defined below.

Note that the :class:`~topology.Mixin1D` and :class:`~topology.Mixin3D` classes add
supplementary functionality specific to 1D
(:class:`~topology.Edge` and :class:`~topology.Wire`) and 3D (:class:`~topology.Compound` and
`~topology.Solid`) objects respectively.
Note that a :class:`~topology.Compound` may be contain only 1D, 2D (:class:`~topology.Face`)  or 3D objects.

.. inheritance-diagram:: topology.shape_core topology.zero_d topology.one_d topology.two_d topology.three_d topology.composite topology.utils
   :parts: 1

.. py:module:: topology

.. autoclass:: Compound
.. autoclass:: Edge
.. autoclass:: Face
   :special-members: __neg__
.. autoclass:: Mixin1D
   :special-members: __matmul__, __mod__
.. autoclass:: Mixin2D
.. autoclass:: Mixin3D
.. autoclass:: Shape
   :special-members: __add__, __sub__, __and__, __rmul__, __eq__, __copy__, __deepcopy__, __hash__
.. autoclass:: ShapeList
   :special-members: __gt__, __lt__, __rshift__, __lshift__, __or__, __and__, __sub__, __getitem__
.. autoclass:: Shell
.. autoclass:: Solid
.. autoclass:: Wire
.. autoclass:: Vertex
   :special-members: __add__, __sub__
.. autoclass:: Curve
   :special-members: __matmul__, __mod__
.. autoclass:: Part
.. autoclass:: Sketch


*************
Import/Export
*************
Methods and functions specific to exporting and importing build123d objects are defined below.

.. py:module:: importers
   :noindex:

.. autofunction:: import_brep
   :noindex:
.. autofunction:: import_step
   :noindex:
.. autofunction:: import_stl
   :noindex:
.. autofunction:: import_svg
   :noindex:
.. autofunction:: import_svg_as_buildline_code
   :noindex:


************
Joint Object
************
Base Joint class which is used to position Solid and Compound objects relative to each
other are defined below. The :ref:`joints` section contains the class description of the
derived Joint classes.

.. py:module:: topology
   :noindex:

.. autoclass:: Joint



================================================
FILE: docs/environment.yaml
================================================
name: docs
channels:
  - conda-forge
  - defaults
dependencies:
  - sphinx
  - nbsphinx
  - pip:
    - sphinx_rtd_theme
    - git+https://github.com/gumyr/build123d.git#egg=build123d



================================================
FILE: docs/examples_1.rst
================================================
#######################
The build123d Examples
#######################
.. |siren| replace:: 🚨
.. |Builder| replace:: 🔨
.. |Algebra| replace:: ✏️

Overview
--------------------------------

In the GitHub repository you will find an `examples folder <https://github.com/42sol-eu/build123d/tree/examples>`_.

Most of the examples show the builder and algebra modes.

.. ----------------------------------------------------------------------------------------------
.. Index Section
.. ----------------------------------------------------------------------------------------------


.. grid:: 3

    .. grid-item-card:: Benchy |Builder|
        :img-top:  assets/examples/thumbnail_benchy_01.png
        :link: examples-benchy
        :link-type: ref

    .. grid-item-card:: Bicycle Tire |Builder|
        :img-top:  assets/examples/bicycle_tire.png
        :link: examples-bicycle_tire
        :link-type: ref

    .. grid-item-card:: Canadian Flag Blowing in The Wind |Builder| |Algebra|
            :img-top: assets/examples/example_canadian_flag_01.png
            :link: examples-canadian_flag
            :link-type: ref

    .. grid-item-card:: Cast Bearing Unit |Builder|
            :img-top: assets/examples/cast_bearing_unit.png
            :link: examples-cast_bearing_unit
            :link-type: ref

    .. grid-item-card:: Circuit Board With Holes |Builder| |Algebra|
            :img-top: assets/examples/thumbnail_circuit_board_01.png
            :link: examples-circuit_board
            :link-type: ref

    .. grid-item-card:: Clock Face |Builder| |Algebra|
            :img-top: assets/examples/clock_face.png
            :link: clock_face
            :link-type: ref

    .. grid-item-card:: Fast Grid Holes |Algebra|
            :img-top: assets/examples/fast_grid_holes.png
            :link: fast_grid_holes
            :link-type: ref

    .. grid-item-card:: Handle |Builder| |Algebra|
            :img-top: assets/examples/handle.png
            :link: handle
            :link-type: ref

    .. grid-item-card:: Heat Exchanger |Builder| |Algebra|
            :img-top: assets/examples/heat_exchanger.png
            :link: heat_exchanger
            :link-type: ref

    .. grid-item-card:: Key Cap |Builder| |Algebra|
            :img-top: assets/examples/key_cap.png
            :link: key_cap
            :link-type: ref

    .. grid-item-card:: (former) build123d Logo |Builder| |Algebra|
            :img-top: assets/examples/thumbnail_build123d_logo_01.png
            :link: examples-build123d_logo
            :link-type: ref

    .. grid-item-card:: Maker Coin |Builder|
            :img-top: assets/examples/maker_coin.png
            :link: maker_coin
            :link-type: ref

    .. grid-item-card:: Multi-Sketch Loft |Builder| |Algebra|
            :img-top: assets/examples/loft.png
            :link: multi_sketch_loft
            :link-type: ref

    .. grid-item-card:: Peg Board J Hook |Builder|  |Algebra|
            :img-top: assets/examples/peg_board_hook.png
            :link: peg_board_hook
            :link-type: ref

    .. grid-item-card:: Platonic Solids |Algebra|
            :img-top: assets/examples/platonic_solids.png
            :link: platonic_solids
            :link-type: ref

    .. grid-item-card:: Playing Cards |Builder|
            :img-top: assets/examples/playing_cards.png
            :link: playing_cards
            :link-type: ref

    .. grid-item-card:: Stud Wall |Algebra|
            :img-top: assets/examples/stud_wall.png
            :link: stud_wall
            :link-type: ref

    .. grid-item-card:: Tea Cup |Builder| |Algebra|
            :img-top: assets/examples/tea_cup.png
            :link: tea_cup
            :link-type: ref

    .. grid-item-card:: Toy Truck |Builder|
            :img-top: assets/examples/toy_truck.png
            :link: toy_truck
            :link-type: ref

    .. grid-item-card:: Vase |Builder| |Algebra|
            :img-top: assets/examples/vase.png
            :link: vase
            :link-type: ref

.. NOTE 01: insert new example thumbnails above this line

.. TODO: Copy this block to add the example thumbnails here
    .. grid-item-card:: name-of-your-example-with-spaces |Builder| |Algebra|
            :img-top: assets/examples/thumbnail_{name-of-your-example}_01.{extension}
            :link: examples-{name-of-your-example}
            :link-type: ref

.. ----------------------------------------------------------------------------------------------
.. Details Section
.. ----------------------------------------------------------------------------------------------

.. _examples-benchy:

Benchy
------
.. image:: assets/examples/example_benchy_01.png
    :align: center


The Benchy examples shows how to import a STL model as a `Solid` object with the class `Mesher` and
modify it by replacing chimney with a BREP version.

- Benchy STL model: :download:`low_poly_benchy.stl <../examples/low_poly_benchy.stl>`


.. note

     *Attribution:*
     The low-poly-benchy used in this example is by `reddaugherty`, see
     https://www.printables.com/model/151134-low-poly-benchy.


.. dropdown:: Gallery

    .. image:: assets/examples/example_benchy_02.png
        :align: center


    .. image:: assets/examples/example_benchy_03.png
        :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/benchy.py
        :start-after: [Code]
        :end-before: [End]

.. ----------------------------------------------------------------------------------------------

.. _examples-bicycle_tire:

Bicycle Tire
--------------------------------
.. image:: assets/examples/bicycle_tire.png
    :align: center

This example demonstrates how to model a realistic bicycle tire with a
patterned tread using build123d. The key concept showcased here is the
use of wrap_faces to project 2D planar geometry onto a curved 3D
surface.

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/bicycle_tire.py
        :start-after: [Code]
        :end-before: [End]

.. _examples-build123d_logo:

Former build123d Logo
--------------------------------
.. image:: assets/examples/example_build123d_logo_01.png
    :align: center


This example creates the former build123d logo (new logo was created in the end of 2023).

Using text and lines to create the first build123d logo.
The builder mode example also generates the SVG file `logo.svg`.


.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/build123d_logo.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/build123d_logo_algebra.py
        :start-after: [Code]
        :end-before: [End]


.. _examples-cast_bearing_unit:

Cast Bearing Unit
-----------------
.. image:: assets/examples/cast_bearing_unit.png
    :align: center

This example demonstrates the creation of a castable flanged bearing housing
using the `draft` operation to add appropriate draft angles for mold release.


.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/cast_bearing_unit.py
        :start-after: [Code]
        :end-before: [End]

.. _examples-canadian_flag:

Canadian Flag Blowing in The Wind
----------------------------------
.. image:: assets/examples/example_canadian_flag_01.png
    :align: center



A Canadian Flag blowing in the wind created by projecting planar faces onto a non-planar face (the_wind).

This example also demonstrates building complex lines that snap to existing features.


.. dropdown:: More Images

    .. image:: assets/examples/example_canadian_flag_02.png
        :align: center

    .. image:: assets/examples/example_canadian_flag_03.png
        :align: center


.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/canadian_flag.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/canadian_flag_algebra.py
        :start-after: [Code]
        :end-before: [End]


.. _examples-circuit_board:


Circuit Board With Holes
------------------------
.. image:: assets/examples/example_circuit_board_01.png
    :align: center



This example demonstrates placing holes around a part.

- Builder mode uses `Locations` context to place the positions.
- Algebra mode uses `product` and `range` to calculate the positions.



.. dropdown:: More Images

    .. image:: assets/examples/example_circuit_board_02.png
        :align: center


.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/circuit_board.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/circuit_board_algebra.py
        :start-after: [Code]
        :end-before: [End]


.. _clock_face:

Clock Face
----------
.. image:: assets/examples/clock_face.png
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/clock.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/clock_algebra.py
        :start-after: [Code]
        :end-before: [End]

The Python code utilizes the build123d library to create a 3D model of a clock face.
It defines a minute indicator with arcs and lines, applying fillets, and then
integrates it into the clock face sketch. The clock face includes a circular outline,
hour labels, and slots at specified positions. The resulting 3D model represents
a detailed and visually appealing clock design.

:class:`~build_common.PolarLocations` are used to position features on the clock face.

.. _fast_grid_holes:

Fast Grid Holes
---------------
.. image:: assets/examples/fast_grid_holes.png
    :align: center

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/fast_grid_holes.py
        :start-after: [Code]
        :end-before: [End]

This example demonstrates an efficient approach to creating a large number of holes
(625 in this case) in a planar part using build123d.

Instead of modeling and subtracting 3D solids for each hole—which is computationally
expensive—this method constructs a 2D Face from an outer perimeter wire and a list of
hole wires. The entire face is then extruded in a single operation to form the final
3D object. This approach significantly reduces modeling time and complexity.

The hexagonal hole pattern is generated using HexLocations, and each location is
populated with a hexagonal wire. These wires are passed directly to the Face constructor
as holes. On a typical Linux laptop, this script completes in approximately 1.02 seconds,
compared to substantially longer runtimes for boolean subtraction of individual holes in 3D.


.. _handle:

Handle
------
.. image:: assets/examples/handle.png
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/handle.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/handle_algebra.py
        :start-after: [Code]
        :end-before: [End]

This example demonstrates multisection sweep creating a drawer handle.

.. _heat_exchanger:

Heat Exchanger
--------------
.. image:: assets/examples/heat_exchanger.png
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/heat_exchanger.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/heat_exchanger_algebra.py
        :start-after: [Code]
        :end-before: [End]

This example creates a model of a parametric heat exchanger core. The positions
of the tubes are defined with :class:`~build_common.HexLocations` and further
limited to fit within the circular end caps. The ends of the tubes are filleted
to the end plates to simulate welding.

.. _key_cap:

Key Cap
-------
.. image:: assets/examples/key_cap.png
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/key_cap.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/key_cap_algebra.py
        :start-after: [Code]
        :end-before: [End]

This example demonstrates the design of a Cherry MX key cap by using
extrude with a taper and extrude until next.

.. _maker_coin:

Maker Coin
----------
.. image:: assets/examples/maker_coin.png
    :align: center

This example creates the maker coin as defined by Angus on the Maker's Muse
YouTube channel. There are two key features:

#. the use of :class:`~objects_curve.DoubleTangentArc` to create a smooth
   transition from the central dish to the outside arc, and

#. embossing the text into the top of the coin not just as a simple
   extrude but from a projection which results in text with even depth.


.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/maker_coin.py
        :start-after: [Code]
        :end-before: [End]


.. _multi_sketch_loft:

Multi-Sketch Loft
-----------------

.. image:: assets/examples/loft.png
    :align: center

This example demonstrates lofting a set of sketches, selecting
the top and bottom by type, and shelling.

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/loft.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/loft_algebra.py
        :start-after: [Code]
        :end-before: [End]


.. _peg_board_hook:

Peg Board Hook
--------------
.. image:: assets/examples/peg_board_hook.png
    :align: center

This script creates a a J-shaped pegboard hook. These hooks are commonly used for
organizing tools in garages, workshops, or other spaces where tools and equipment
need to be stored neatly and accessibly. The hook is created by defining a complex
path and then sweeping it to define the hook. The sides of the hook are flattened
to aid 3D printing.

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/pegboard_j_hook.py
        :start-after: [Code]
        :end-before: [End]


.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/pegboard_j_hook_algebra.py
        :start-after: [Code]
        :end-before: [End]


.. _platonic_solids:

Platonic Solids
---------------
.. image:: assets/examples/platonic_solids.png
    :align: center

This example creates a custom Part object PlatonicSolid.

Platonic solids are five three-dimensional shapes that are highly symmetrical,
known since antiquity and named after the ancient Greek philosopher Plato.
These solids are unique because their faces are congruent regular polygons,
with the same number of faces meeting at each vertex. The five Platonic solids
are the tetrahedron (4 triangular faces), cube (6 square faces), octahedron
(8 triangular faces), dodecahedron (12 pentagonal faces), and icosahedron
(20 triangular faces). Each solid represents a unique way in which identical
polygons can be arranged in three dimensions to form a convex polyhedron,
embodying ideals of symmetry and balance.

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/platonic_solids.py
        :start-after: [Code]
        :end-before: [End]

.. _playing_cards:

Playing Cards
-------------
.. image:: assets/examples/playing_cards.png
    :align: center

This example creates a customs Sketch objects: Club, Spade, Heart, Diamond,
and PlayingCard in addition to a two part playing card box which has suit
cutouts in the lid. The four suits are created with Bézier curves that were
imported as code from an SVG file and modified to the code found here.

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/playing_cards.py
        :start-after: [Code]
        :end-before: [End]

.. _stud_wall:

Stud Wall
---------
.. image:: assets/examples/stud_wall.png
    :align: center

This example demonstrates creating custom `Part` objects and putting them into
assemblies. The custom object is a `Stud` used in the building industry while
the assembly is a `StudWall` created from copies of `Stud` objects for efficiency.
Both the `Stud` and `StudWall` objects use `RigidJoints` to define snap points which
are used to position all of objects.

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/stud_wall.py
        :start-after: [Code]
        :end-before: [End]

.. _tea_cup:

Tea Cup
-------
.. image:: assets/examples/tea_cup.png
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/tea_cup.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/tea_cup_algebra.py
        :start-after: [Code]
        :end-before: [End]

This example demonstrates the creation a tea cup, which serves as an example of
constructing complex, non-flat geometrical shapes programmatically.

The tea cup model involves several CAD techniques, such as:

* Revolve Operations: There is 1 occurrence of a revolve operation. This is used
  to create the main body of the tea cup by revolving a profile around an axis,
  a common technique for generating symmetrical objects like cups.
* Sweep Operations: There are 2 occurrences of sweep operations. The handle are
  created by sweeping a profile along a path to generate non-planar surfaces.
* Offset/Shell Operations: the bowl of the cup is hollowed out with the offset
  operation leaving the top open.
* Fillet Operations: There is 1 occurrence of a fillet operation which is used to
  round the edges for aesthetic improvement and to mimic real-world objects more
  closely.


.. _toy_truck:

Toy Truck
---------
.. image:: assets/examples/toy_truck.png
    :align: center

.. image:: assets/examples/toy_truck_picture.jpg
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/toy_truck.py
        :start-after: [Code]
        :end-before: [End]

This example demonstrates how to design a toy truck using BuildPart and
BuildSketch in Builder mode. The model includes a detailed body, cab, grill,
and bumper, showcasing techniques like sketch reuse, symmetry, tapered
extrusions, selective filleting, and the use of joints for part assembly.
Ideal for learning complex part construction and hierarchical modeling in
build123d.

.. _vase:

Vase
----
.. image:: assets/examples/vase.png
    :align: center

.. dropdown:: |Builder| Reference Implementation (Builder Mode)

    .. literalinclude:: ../examples/vase.py
        :start-after: [Code]
        :end-before: [End]

.. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

    .. literalinclude:: ../examples/vase_algebra.py
        :start-after: [Code]
        :end-before: [End]

This example demonstrates the build123d techniques involving the creation of a vase.
Specifically, it showcases the processes of revolving a sketch, shelling
(creating a hollow object by removing material from its interior), and
selecting edges by position range and type for the application of fillets
(rounding off the edges).

* Sketching: Drawing a 2D profile or outline that represents the side view of
  the vase.
* Revolving: Rotating the sketch around an axis to create a 3D object. This
  step transforms the 2D profile into a 3D vase shape.
* Offset/Shelling: Removing material from the interior of the solid vase to
  create a hollow space, making it resemble a real vase more closely.
* Edge Filleting: Selecting specific edges of the vase for filleting, which
  involves rounding those edges. The edges are selected based on their position
  and type.


.. NOTE 02: insert new example thumbnails above this line


.. TODO: Copy this block to add your example details here
    .. _examples-{name-of-your-example}:

    {name-of-your-example-with-spaces}
    --------------------------------
    .. image:: assets/examples/example_{name-of-your-example}_01.{extension}
    :align: center

    .. image:: assets/examples/example_{name-of-your-example}_02.{extension}
    :align: center

    .. dropdown:: info

        TODO: add more information about your example

    .. dropdown:: |Builder| Reference Implementation (Builder Mode)

        .. literalinclude:: ../examples/boxes_on_faces.py
            :start-after: [Code]
            :end-before: [End]

    .. dropdown:: |Algebra| Reference Implementation (Algebra Mode)

        .. literalinclude:: ../examples/boxes_on_faces_algebra.py
            :start-after: [Code]
            :end-before: [End]



================================================
FILE: docs/external.rst
================================================
.. _external:

############################
External Tools and Libraries
############################

The following sections describe tools and libraries external to build123d
that extend its functionality.

*****************
Editors & Viewers
*****************

ocp-vscode
==========

A viewer for OCP based Code-CAD (CadQuery, build123d) integrated into
VS Code.

See: `ocp-vscode <https://github.com/bernhard-42/vscode-ocp-cad-viewer>`_
(formerly known as cq_vscode)

Watch Jern create three build123d designs in realtime with Visual
Studio Code and the ocp-vscode viewer extension in a timed event from the TooTallToby 2024 Spring Open Tournament: 
`build123d entry video <https://www.youtube.com/watch?v=UhUmMInlJic>`_

cq-editor fork
==============

GUI editor based on PyQT. This fork has changes from jdegenstein to allow easier use with build123d.

See: `jdegenstein's fork of cq-editor <https://github.com/jdegenstein/jmwright-CQ-Editor>`_

Yet Another CAD Viewer
======================

A web-based CAD viewer for OCP models (CadQuery/build123d) that runs in any modern browser and supports
static site deployment. Features include interactive inspection of faces, edges, and vertices, 
measurement tools, per-model clipping planes, transparency control, and hot reloading via ``yacv-server``. 
It also has a build123d playground for editing and sharing models directly in the browser 
(`demo <https://yeicor-3d.github.io/yet-another-cad-viewer/#pg_code_url=https://raw.githubusercontent.com/gumyr/build123d/refs/heads/dev/examples/toy_truck.py>`_).

See: `Yet Another CAD Viewer <https://github.com/yeicor-3d/yet-another-cad-viewer>`_

PartCAD VS Code extension
=========================

A wrapper around ``ocp-vscode`` (see above) which requires build123d scripts to be
packaged using ``PartCAD`` (see below). While it requires the overhead of maintaining
the package, it provides some convenience features (such as UI controls to export models)
as well as functional features (such as UI controls to pass parameters into build123d scripts
and AI-based generative design tools).

It's also the most convenient tool to create new packages and parts. More PDM and PLM features are expected to arrive soon.

**************
Part Libraries
**************

bd_warehouse
============

On-demand generation of parametric parts that seamlessly integrate into
build123d projects.

Parts available include:

    * fastener - Nuts, Screws, Washers and custom holes
    * flange - Standardized parametric flanges
    * pipe - Standardized parametric pipes
    * thread - Parametric helical threads (Iso, Acme, Plastic, etc.)

See: `bd_warehouse <https://bd-warehouse.readthedocs.io/en/latest/index.html>`_

bd_beams_and_bars
=================

2D sections and 3D beams generation (UPN, IPN, UPE, flat bars, ...)

See: `bd_beams_and_bars <https://bd-beams-and-bars.3d.experimentslabs.com/>`_

Superellipses & Superellipsoids
===============================

Superellipses are a more sophisticated alternative to rounded
rectangles, with smoothly changing curvature. They are flexible
shapes that can be adjusted by changing the "exponent" to get a
result that varies between rectangular and elliptical, or from
square, through squircle, to circle, and beyond...

Superellipses can be found:

  * in typefaces such as Melior, Eurostyle, and Computer Modern
  * as the shape of airliner windows, tables, plates
  * clipping the outline of iOS app icons

They were named and popularized in the 1950s-1960s by the Danish
mathematician and poet Piet Hein, who used them in the winning
design for the Sergels Torg roundabout in Stockholm.

See: `Superellipses & Superellipsoids <https://github.com/fanf2/kbd/blob/model-b/keybird42/superellipse.py>`_

Public PartCAD repository
=========================

See `partcad.org <https://partcad.org/repository>`_ for all the models packaged and published
using ``PartCAD`` (see below). This repository contains individual parts,
as well as large assemblies created using those parts. See
`the OpenVMP robot <https://partcad.org/repository/package/robotics/multimodal/openvmp/robots/don1>`_
as an example of an assembly

gggears generator
=================
A gear generation framework that allows easy creation of a wide range of gears and drives.

See `gggears <https://github.com/GarryBGoode/gggears>`_

*****
Tools
*****

blendquery
==========

CadQuery and build123d integration for Blender.

See: `blendquery <https://github.com/uki-dev/blendquery>`_

nething
=======

3D generative AI for CAD modeling. Now everyone is an engineer. Make your ideas real.

See: `nething <https://nething.xyz/>`_

Listen to the following podcast which discusses **nething** in detail:
`The Next Byte Podcast <https://pod.link/wevolver/episode/74b11c1ff2bfc977adc96e5c7b4cd162>`_

ocp-freecad-cam
===============

CAM for CadQuery and Build123d by leveraging FreeCAD library. Visualizes in CQ-Editor 
and ocp-cad-viewer. Spiritual successor of `cq-cam <https://github.com/voneiden/cq-cam>`_

See: `ocp-freecad-cam <https://github.com/voneiden/ocp-freecad-cam>`_

PartCAD
=======

A package manager for CAD models. Build123d is the most supported Code-CAD framework,
but CadQuery and OpenSCAD are also supported. It can be used by build123d designs
`to import parts <https://partcad.readthedocs.io/en/latest/use_cases.html#python-build123d>`_
from PartCAD repositories, and to
`publish build123d designs <https://partcad.readthedocs.io/en/latest/use_cases.html#publish-packages>`_
to be consumed by others.

dl4to4ocp
=========

Library that helps perform `topology optimization <https://en.wikipedia.org/wiki/Topology_optimization>`_ on
your `OCP <https://github.com/CadQuery/OCP>`_-based CAD
models (`CadQuery <https://github.com/CadQuery/cadquery>`_/`Build123d <https://github.com/gumyr/build123d>`_/...) using
the `dl4to <https://github.com/dl4to/dl4to>`_ library.

See: `dl4to4ocp <https://github.com/yeicor-3d/dl4to4ocp/>`_

OCP.wasm
========

This project ports the low-level dependencies required for build123d to run in a browser. 
For a fully featured frontend, check out ``Yet Another CAD Viewer`` (see above).

See: `OCP.wasm <https://github.com/yeicor/OCP.wasm>`_



================================================
FILE: docs/general_examples.py
================================================
"""

name: general_examples.py
by:   jdegenstein
date: December 29th 2022

desc:

    This is the build123d general examples python script. It generates the SVGs
    when run as a script, and is pulled into sphinx docs by
    tutorial_general.rst.

license:

    Copyright 2022 jdegenstein

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from build123d import *


def write_svg():
    """Save an image of the BuildPart object as SVG"""
    global example_counter
    try:
        example_counter += 1
    except:
        example_counter = 1

    builder: BuildPart = BuildPart._get_context()

    visible, hidden = builder.part.project_to_viewport((-100, -100, 70))
    max_dimension = max(*Compound(children=visible + hidden).bounding_box().size)
    exporter = ExportSVG(scale=100 / max_dimension)
    exporter.add_layer("Visible")
    exporter.add_layer("Hidden", line_color=(99, 99, 99), line_type=LineType.ISO_DOT)
    exporter.add_shape(visible, layer="Visible")
    exporter.add_shape(hidden, layer="Hidden")
    exporter.write(f"assets/general_ex{example_counter}.svg")


##########################################
# 1. Simple Rectangular Plate
# [Ex. 1]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex1:
    Box(length, width, thickness)
    # [Ex. 1]
    write_svg()

# show_object(ex1.part)


##########################################
# 2. Plane with Hole
# [Ex. 2]
length, width, thickness = 80.0, 60.0, 10.0
center_hole_dia = 22.0

with BuildPart() as ex2:
    Box(length, width, thickness)
    Cylinder(radius=center_hole_dia / 2, height=thickness, mode=Mode.SUBTRACT)
    # [Ex. 2]
    write_svg()

# show_object(ex2.part)

##########################################
# 3. An extruded prismatic solid
# [Ex. 3]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex3:
    with BuildSketch() as ex3_sk:
        Circle(width)
        Rectangle(length / 2, width / 2, mode=Mode.SUBTRACT)
    extrude(amount=2 * thickness)
    # [Ex. 3]
    write_svg()

# show_object(ex3.part)

##########################################
# Building Profiles using lines and arcs
# [Ex. 4]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex4:
    with BuildSketch() as ex4_sk:
        with BuildLine() as ex4_ln:
            l1 = Line((0, 0), (length, 0))
            l2 = Line((length, 0), (length, width))
            l3 = ThreePointArc((length, width), (width, width * 1.5), (0.0, width))
            l4 = Line((0.0, width), (0, 0))
        make_face()
    extrude(amount=thickness)
    # [Ex. 4]
    write_svg()

# show_object(ex4.part)

##########################################
# Moving The Current working point
# [Ex. 5]
a, b, c, d = 90, 45, 15, 7.5

with BuildPart() as ex5:
    with BuildSketch() as ex5_sk:
        Circle(a)
        with Locations((b, 0.0)):
            Rectangle(c, c, mode=Mode.SUBTRACT)
        with Locations((0, b)):
            Circle(d, mode=Mode.SUBTRACT)
    extrude(amount=c)
    # [Ex. 5]
    write_svg()

# show_object(ex5.part)

##########################################
# Using Point Lists
# [Ex. 6]
a, b, c = 80, 60, 10

with BuildPart() as ex6:
    with BuildSketch() as ex6_sk:
        Circle(a)
        with Locations((b, 0), (0, b), (-b, 0), (0, -b)):
            Circle(c, mode=Mode.SUBTRACT)
    extrude(amount=c)
    # [Ex. 6]
    write_svg()

# show_object(ex6.part)
#############################
# Polygons
# [Ex. 7]
a, b, c = 60, 80, 5

with BuildPart() as ex7:
    with BuildSketch() as ex7_sk:
        Rectangle(a, b)
        with Locations((0, 3 * c), (0, -3 * c)):
            RegularPolygon(radius=2 * c, side_count=6, mode=Mode.SUBTRACT)
    extrude(amount=c)
    # [Ex. 7]
    write_svg()

# show_object(ex7.part)

##########################################
# 8. Polylines
# [Ex. 8]
(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)
pts = [
    (0, H / 2.0),
    (W / 2.0, H / 2.0),
    (W / 2.0, (H / 2.0 - t)),
    (t / 2.0, (H / 2.0 - t)),
    (t / 2.0, (t - H / 2.0)),
    (W / 2.0, (t - H / 2.0)),
    (W / 2.0, H / -2.0),
    (0, H / -2.0),
]

with BuildPart() as ex8:
    with BuildSketch(Plane.YZ) as ex8_sk:
        with BuildLine() as ex8_ln:
            Polyline(pts)
            mirror(ex8_ln.line, about=Plane.YZ)
        make_face()
    extrude(amount=L)
    # [Ex. 8]
    write_svg()

# show_object(ex8.part)

##########################################
# 9. Selectors, fillets, and chamfers
# [Ex. 9]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex9:
    Box(length, width, thickness)
    chamfer(ex9.edges().group_by(Axis.Z)[-1], length=4)
    fillet(ex9.edges().filter_by(Axis.Z), radius=5)
    # [Ex. 9]
    write_svg()

# show_object(ex9.part)

##########################################
# 10. Select Last and Hole
# [Ex. 10]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex10:
    Box(length, width, thickness)
    Hole(radius=width / 4)
    fillet(ex10.edges(Select.LAST).group_by(Axis.Z)[-1], radius=2)
    # [Ex. 10]
    write_svg()

# show_object(ex10.part)

##########################################
# 11. Use a face as workplane for BuildSketch and introduce GridLocations
# [Ex. 11]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex11:
    Box(length, width, thickness)
    chamfer(ex11.edges().group_by(Axis.Z)[-1], length=4)
    fillet(ex11.edges().filter_by(Axis.Z), radius=5)
    Hole(radius=width / 4)
    fillet(ex11.edges(Select.LAST).sort_by(Axis.Z)[-1], radius=2)
    with BuildSketch(ex11.faces().sort_by(Axis.Z)[-1]) as ex11_sk:
        with GridLocations(length / 2, width / 2, 2, 2):
            RegularPolygon(radius=5, side_count=5)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
    # [Ex. 11]
    write_svg()

# show_object(ex11)

##########################################
# 12. Defining an Edge with a Spline
# [Ex. 12]
pts = [
    (55, 30),
    (50, 35),
    (40, 30),
    (30, 20),
    (20, 25),
    (10, 20),
    (0, 20),
]

with BuildPart() as ex12:
    with BuildSketch() as ex12_sk:
        with BuildLine() as ex12_ln:
            l1 = Spline(pts)
            l2 = Line((55, 30), (60, 0))
            l3 = Line((60, 0), (0, 0))
            l4 = Line((0, 0), (0, 20))
        make_face()
    extrude(amount=10)
    # [Ex. 12]
    write_svg()

# show_object(ex12.part)


##########################################
# 13. CounterBoreHoles, CounterSinkHoles and PolarLocations
# [Ex. 13]
a, b = 40, 4
with BuildPart() as ex13:
    Cylinder(radius=50, height=10)
    with Locations(ex13.faces().sort_by(Axis.Z)[-1]):
        with PolarLocations(radius=a, count=4):
            CounterSinkHole(radius=b, counter_sink_radius=2 * b)
        with PolarLocations(radius=a, count=4, start_angle=45, angular_range=360):
            CounterBoreHole(radius=b, counter_bore_radius=2 * b, counter_bore_depth=b)
    # [Ex. 13]
    write_svg()

# show_object(ex13.part)

##########################################
# 14. Position on a line with '@', '%' and introduce sweep
# [Ex. 14]
a, b = 40, 20

with BuildPart() as ex14:
    with BuildLine() as ex14_ln:
        l1 = JernArc(start=(0, 0), tangent=(0, 1), radius=a, arc_size=180)
        l2 = JernArc(start=l1 @ 1, tangent=l1 % 1, radius=a, arc_size=-90)
        l3 = Line(l2 @ 1, l2 @ 1 + (-a, a))
    with BuildSketch(Plane.XZ) as ex14_sk:
        Rectangle(b, b)
    sweep()
    # [Ex. 14]
    write_svg()

# show_object(ex14.part)


##########################################
# 15. Mirroring Symmetric Geometry
# [Ex. 15]
a, b, c = 80, 40, 20

with BuildPart() as ex15:
    with BuildSketch() as ex15_sk:
        with BuildLine() as ex15_ln:
            l1 = Line((0, 0), (a, 0))
            l2 = Line(l1 @ 1, l1 @ 1 + (0, b))
            l3 = Line(l2 @ 1, l2 @ 1 + (-c, 0))
            l4 = Line(l3 @ 1, l3 @ 1 + (0, -c))
            l5 = Line(l4 @ 1, (0, (l4 @ 1).Y))
            mirror(ex15_ln.line, about=Plane.YZ)
        make_face()
    extrude(amount=c)
    # [Ex. 15]
    write_svg()

# show_object(ex15.part)

##########################################
# 16. Mirroring 3D Objects
# same concept as CQ docs, but different object
# [Ex. 16]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex16_single:
    with BuildSketch(Plane.XZ) as ex16_sk:
        Rectangle(length, width)
        fillet(ex16_sk.vertices(), radius=length / 10)
        with GridLocations(x_spacing=length / 4, y_spacing=0, x_count=3, y_count=1):
            Circle(length / 12, mode=Mode.SUBTRACT)
        Rectangle(length, width, align=(Align.MIN, Align.MIN), mode=Mode.SUBTRACT)
    extrude(amount=length)

with BuildPart() as ex16:
    add(ex16_single.part)
    mirror(ex16_single.part, about=Plane.XY.offset(width))
    mirror(ex16_single.part, about=Plane.YX.offset(width))
    mirror(ex16_single.part, about=Plane.YZ.offset(width))
    mirror(ex16_single.part, about=Plane.YZ.offset(-width))
    # [Ex. 16]
    write_svg()

# show_object(ex16.part)

##########################################
# 17. Mirroring From Faces
# [Ex. 17]
a, b = 30, 20

with BuildPart() as ex17:
    with BuildSketch() as ex17_sk:
        RegularPolygon(radius=a, side_count=5)
    extrude(amount=b)
    mirror(ex17.part, about=Plane(ex17.faces().group_by(Axis.Y)[0][0]))
    # [Ex. 17]
    write_svg()

# show_object(ex17.part)

##########################################
# 18. Creating Workplanes on Faces
# based on Ex. 9
# [Ex. 18]
length, width, thickness = 80.0, 60.0, 10.0
a, b = 4, 5

with BuildPart() as ex18:
    Box(length, width, thickness)
    chamfer(ex18.edges().group_by(Axis.Z)[-1], length=a)
    fillet(ex18.edges().filter_by(Axis.Z), radius=b)
    with BuildSketch(ex18.faces().sort_by(Axis.Z)[-1]):
        Rectangle(2 * b, 2 * b)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
    # [Ex. 18]
    write_svg()

# show_object(ex18.part)

##########################################
# 19. Locating a Workplane on a vertex
# [Ex. 19]
length, thickness = 80.0, 10.0

with BuildPart() as ex19:
    with BuildSketch() as ex19_sk:
        RegularPolygon(radius=length / 2, side_count=7)
    extrude(amount=thickness)
    topf = ex19.faces().sort_by(Axis.Z)[-1]
    vtx = topf.vertices().group_by(Axis.X)[-1][0]
    vtx2Axis = Axis((0, 0, 0), (-1, -0.5, 0))
    vtx2 = topf.vertices().sort_by(vtx2Axis)[-1]
    with BuildSketch(topf) as ex19_sk2:
        with Locations((vtx.X, vtx.Y), (vtx2.X, vtx2.Y)):
            Circle(radius=length / 8)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
    # [Ex. 19]
    write_svg()

# show_object(ex19.part)

##########################################
# 20. Offset Sketch Workplane
# [Ex. 20]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex20:
    Box(length, width, thickness)
    plane = Plane(ex20.faces().group_by(Axis.X)[0][0])
    with BuildSketch(plane.offset(2 * thickness)):
        Circle(width / 3)
    extrude(amount=width)
    # [Ex. 20]
    write_svg()

# show_object(ex20.part)

##########################################
# 21. Copying Workplanes
# [Ex. 21]
width, length = 10.0, 60.0

with BuildPart() as ex21:
    with BuildSketch() as ex21_sk:
        Circle(width / 2)
    extrude(amount=length)
    with BuildSketch(Plane(origin=ex21.part.center(), z_dir=(-1, 0, 0))):
        Circle(width / 2)
    extrude(amount=length)
    # [Ex. 21]
    write_svg()

# show_object(ex21.part)

##########################################
# 22. Rotated Workplanes
# [Ex. 22]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex22:
    Box(length, width, thickness)
    pln = Plane(ex22.faces().group_by(Axis.Z)[0][0]).rotated((0, -50, 0))
    with BuildSketch(pln) as ex22_sk:
        with GridLocations(length / 4, width / 4, 2, 2):
            Circle(thickness / 4)
    extrude(amount=-100, both=True, mode=Mode.SUBTRACT)
    # [Ex. 22]
    write_svg()

# show_object(ex22.part)

##########################################
# 23. Revolve
# [Ex. 23]
pts = [
    (-25, 35),
    (-25, 0),
    (-20, 0),
    (-20, 5),
    (-15, 10),
    (-15, 35),
]

with BuildPart() as ex23:
    with BuildSketch(Plane.XZ) as ex23_sk:
        with BuildLine() as ex23_ln:
            l1 = Polyline(pts)
            l2 = Line(l1 @ 1, l1 @ 0)
        make_face()
        with Locations((0, 35)):
            Circle(25)
        split(bisect_by=Plane.ZY)
    revolve(axis=Axis.Z)
    # [Ex. 23]
    write_svg()

# show_object(ex23.part)

##########################################
# 24. Lofts
# [Ex. 24]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex24:
    Box(length, length, thickness)
    with BuildSketch(ex24.faces().group_by(Axis.Z)[0][0]) as ex24_sk:
        Circle(length / 3)
    with BuildSketch(ex24_sk.faces()[0].offset(length / 2)) as ex24_sk2:
        Rectangle(length / 6, width / 6)
    loft()
    # [Ex. 24]
    write_svg()

# show_object(ex24.part)

##########################################
# 25. Offset Sketch
# [Ex. 25]
rad, offs = 50, 10

with BuildPart() as ex25:
    with BuildSketch() as ex25_sk1:
        RegularPolygon(radius=rad, side_count=5)
    with BuildSketch(Plane.XY.offset(15)) as ex25_sk2:
        RegularPolygon(radius=rad, side_count=5)
        offset(amount=offs)
    with BuildSketch(Plane.XY.offset(30)) as ex25_sk3:
        RegularPolygon(radius=rad, side_count=5)
        offset(amount=offs, kind=Kind.INTERSECTION)
    extrude(amount=1)
    # [Ex. 25]
    write_svg()

# show_object(ex25.part)

##########################################
# 26. Offset Part To Create Thin features
# [Ex. 26]
length, width, thickness, wall = 80.0, 60.0, 10.0, 2.0

with BuildPart() as ex26:
    Box(length, width, thickness)
    topf = ex26.faces().sort_by(Axis.Z)[-1]
    offset(amount=-wall, openings=topf)
    # [Ex. 26]
    write_svg()

# show_object(ex26.part)

##########################################
# 27. Splitting an Object
# [Ex. 27]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex27:
    Box(length, width, thickness)
    with BuildSketch(ex27.faces().sort_by(Axis.Z)[0]) as ex27_sk:
        Circle(width / 4)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
    split(bisect_by=Plane(ex27.faces().sort_by(Axis.Y)[-1]).offset(-width / 2))
    # [Ex. 27]
    write_svg()

# show_object(ex27.part)

##########################################
# 28. Locating features based on Faces
# [Ex. 28]
width, thickness = 80.0, 10.0

with BuildPart() as ex28:
    with BuildSketch() as ex28_sk:
        RegularPolygon(radius=width / 4, side_count=3)
    ex28_ex = extrude(amount=thickness, mode=Mode.PRIVATE)
    midfaces = ex28_ex.faces().group_by(Axis.Z)[1]
    Sphere(radius=width / 2)
    for face in midfaces:
        with Locations(face):
            Hole(thickness / 2)
    # [Ex. 28]
    write_svg()

# show_object(ex28.part)

##########################################
# 29. The Classic OCC Bottle
# [Ex. 29]
L, w, t, b, h, n = 60.0, 18.0, 9.0, 0.9, 90.0, 6.0

with BuildPart() as ex29:
    with BuildSketch(Plane.XY.offset(-b)) as ex29_ow_sk:
        with BuildLine() as ex29_ow_ln:
            l1 = Line((0, 0), (0, w / 2))
            l2 = ThreePointArc(l1 @ 1, (L / 2.0, w / 2.0 + t), (L, w / 2.0))
            l3 = Line(l2 @ 1, ((l2 @ 1).X, 0, 0))
            mirror(ex29_ow_ln.line)
        make_face()
    extrude(amount=h + b)
    fillet(ex29.edges(), radius=w / 6)
    with BuildSketch(ex29.faces().sort_by(Axis.Z)[-1]):
        Circle(t)
    extrude(amount=n)
    necktopf = ex29.faces().sort_by(Axis.Z)[-1]
    offset(ex29.solids()[0], amount=-b, openings=necktopf)
    # [Ex. 29]
    write_svg()

# show_object(ex29.part)

##########################################
# 30. Bezier Curve
# [Ex. 30]
pts = [
    (0, 0),
    (20, 20),
    (40, 0),
    (0, -40),
    (-60, 0),
    (0, 100),
    (100, 0),
]

wts = [
    1.0,
    1.0,
    2.0,
    3.0,
    4.0,
    2.0,
    1.0,
]

with BuildPart() as ex30:
    with BuildSketch() as ex30_sk:
        with BuildLine() as ex30_ln:
            l0 = Polyline(pts)
            l1 = Bezier(pts, weights=wts)
        make_face()
    extrude(amount=10)
    # [Ex. 30]
    write_svg()

# show_object(ex30.part)

##########################################
# 31. Nesting Locations
# [Ex. 31]
a, b, c = 80.0, 5.0, 3.0

with BuildPart() as ex31:
    with BuildSketch() as ex31_sk:
        with PolarLocations(a / 2, 6):
            with GridLocations(3 * b, 3 * b, 2, 2):
                RegularPolygon(b, 3)
            RegularPolygon(b, 4)
        RegularPolygon(3 * b, 6, rotation=30)
    extrude(amount=c)
    # [Ex. 31]
    write_svg()

# show_object(ex31.part)

##########################################
# 32. Python for-loop
# [Ex. 32]
a, b, c = 80.0, 10.0, 1.0

with BuildPart() as ex32:
    with BuildSketch(mode=Mode.PRIVATE) as ex32_sk:
        RegularPolygon(2 * b, 6, rotation=30)
        with PolarLocations(a / 2, 6):
            RegularPolygon(b, 4)
    for idx, obj in enumerate(ex32_sk.sketch.faces()):
        add(obj)
        extrude(amount=c + 3 * idx)
    # [Ex. 32]
    write_svg()

# show_object(ex32.part)

##########################################
# 33. Python function and for-loop
# [Ex. 33]
a, b, c = 80.0, 5.0, 1.0


def square(rad, loc):
    with BuildSketch() as sk:
        with Locations(loc):
            RegularPolygon(rad, 4)
    return sk.sketch


with BuildPart() as ex33:
    with BuildSketch(mode=Mode.PRIVATE) as ex33_sk:
        locs = PolarLocations(a / 2, 6)
        for i, j in enumerate(locs):
            add(square(b + 2 * i, j))
    for idx, obj in enumerate(ex33_sk.sketch.faces()):
        add(obj)
        extrude(amount=c + 2 * idx)
    # [Ex. 33]
    write_svg()

# show_object(ex33.part)

##########################################
# 34. Embossed and Debossed Text
# [Ex. 34]
length, width, thickness, fontsz, fontht = 80.0, 60.0, 10.0, 25.0, 4.0

with BuildPart() as ex34:
    Box(length, width, thickness)
    topf = ex34.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(topf) as ex34_sk:
        Text("Hello", font_size=fontsz, align=(Align.CENTER, Align.MIN))
    extrude(amount=fontht)
    with BuildSketch(topf) as ex34_sk2:
        Text("World", font_size=fontsz, align=(Align.CENTER, Align.MAX))
    extrude(amount=-fontht, mode=Mode.SUBTRACT)
    # [Ex. 34]
    write_svg()

# show_object(ex34.part)

##########################################
# 35. Slots
# [Ex. 35]
length, width, thickness = 80.0, 60.0, 10.0

with BuildPart() as ex35:
    Box(length, length, thickness)
    topf = ex35.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(topf) as ex35_sk:
        SlotCenterToCenter(width / 2, 10)
        with BuildLine(mode=Mode.PRIVATE) as ex35_ln:
            RadiusArc((-width / 2, 0), (0, width / 2), radius=width / 2)
        SlotArc(arc=ex35_ln.edges()[0], height=thickness, rotation=0)
        with BuildLine(mode=Mode.PRIVATE) as ex35_ln2:
            RadiusArc((0, -width / 2), (width / 2, 0), radius=-width / 2)
        SlotArc(arc=ex35_ln2.edges()[0], height=thickness, rotation=0)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
    # [Ex. 35]
    write_svg()

# show_object(ex35.part)

##########################################
# 36. Extrude-Until
# [Ex. 36]
rad, rev = 6, 50

with BuildPart() as ex36:
    with BuildSketch() as ex36_sk:
        with Locations((0, rev)):
            Circle(rad)
    revolve(axis=Axis.X, revolution_arc=180)
    with BuildSketch() as ex36_sk2:
        Rectangle(rad, rev)
    extrude(until=Until.NEXT)
    # [Ex. 36]
    write_svg()

# show_object(ex36.part)



================================================
FILE: docs/general_examples_algebra.py
================================================
"""

name: general_examples_algebra.py
by:   Bernhard Walter
date: March 2023

desc:

    This is the build123d general examples python script. It generates the SVGs
    when run as a script, and is pulled into sphinx docs by
    tutorial_general.rst.

license:

    Copyright 2022 jdegenstein

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from build123d import *


##########################################
# 1. Simple Rectangular Plate
# [Ex. 1]
length, width, thickness = 80.0, 60.0, 10.0

ex1 = Box(length, width, thickness)
# [Ex. 1]
# show_object(ex1)


##########################################
# 2. Plane with hole
# [Ex. 2]
length, width, thickness = 80.0, 60.0, 10.0
center_hole_dia = 22.0

ex2 = Box(length, width, thickness)
ex2 -= Cylinder(center_hole_dia / 2, height=thickness)
# [Ex. 2]
# show_object(ex2)

##########################################
# 3. An extruded prismatic solid
# [Ex. 3]
length, width, thickness = 80.0, 60.0, 10.0

sk3 = Circle(width) - Rectangle(length / 2, width / 2)
ex3 = extrude(sk3, amount=2 * thickness)
# [Ex. 3]
# show_object(ex3)

##########################################
# Building profiles using lines and arcs
# [Ex. 4]
length, width, thickness = 80.0, 60.0, 10.0

lines = Curve() + [
    Line((0, 0), (length, 0)),
    Line((length, 0), (length, width)),
    ThreePointArc((length, width), (width, width * 1.5), (0.0, width)),
    Line((0.0, width), (0, 0)),
]
sk4 = make_face(lines)
ex4 = extrude(sk4, thickness)
# [Ex. 4]
# show_object(ex4)

##########################################
# Moving the current working point
# [Ex. 5]
a, b, c, d = 90, 45, 15, 7.5

sk5 = Circle(a) - Pos(b, 0.0) * Rectangle(c, c) - Pos(0.0, b) * Circle(d)
ex5 = extrude(sk5, c)
# [Ex. 5]
# show_object(ex5)

##########################################
# Using Point Lists
# [Ex. 6]
a, b, c = 80, 60, 10

sk6 = [loc * Circle(c) for loc in Locations((b, 0), (0, b), (-b, 0), (0, -b))]
ex6 = extrude(Circle(a) - sk6, c)
# [Ex. 6]
# show_object(ex6)
#################################
# Polygons
# [Ex. 7]
a, b, c = 60, 80, 5

polygons = [
    loc * RegularPolygon(radius=2 * c, side_count=6)
    for loc in Locations((0, 3 * c), (0, -3 * c))
]
sk7 = Rectangle(a, b) - polygons
ex7 = extrude(sk7, amount=c)
# [Ex. 7]
# show_object(ex7)

##########################################
# 8. Polylines
# [Ex. 8]
(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)
pts = [
    (0, H / 2.0),
    (W / 2.0, H / 2.0),
    (W / 2.0, (H / 2.0 - t)),
    (t / 2.0, (H / 2.0 - t)),
    (t / 2.0, (t - H / 2.0)),
    (W / 2.0, (t - H / 2.0)),
    (W / 2.0, H / -2.0),
    (0, H / -2.0),
]

ln = Polyline(pts)
ln += mirror(ln, Plane.YZ)

sk8 = make_face(Plane.YZ * ln)
ex8 = extrude(sk8, -L).clean()
# [Ex. 8]
# show_object(ex8)

##########################################
# 9. Selectors, fillets, and chamfers
# [Ex. 9]
length, width, thickness = 80.0, 60.0, 10.0

ex9 = Part() + Box(length, width, thickness)
ex9 = chamfer(ex9.edges().group_by(Axis.Z)[-1], length=4)
ex9 = fillet(ex9.edges().filter_by(Axis.Z), radius=5)
# [Ex. 9]
# show_object(ex9)

##########################################
# 10. Select last edges and Hole
# [Ex. 10]
ex10 = Part() + Box(length, width, thickness)

snapshot = ex10.edges()
ex10 -= Hole(radius=width / 4, depth=thickness)
last_edges = ex10.edges() - snapshot
ex10 = fillet(last_edges.group_by(Axis.Z)[-1], 2)
# [Ex. 10]
# show_object(ex10)

##########################################
# 11. Use a face as workplane for BuildSketch and introduce GridLocations
# [Ex. 11]
length, width, thickness = 80.0, 60.0, 10.0

ex11 = Part() + Box(length, width, thickness)
ex11 = chamfer(ex11.edges().group_by()[-1], 4)
ex11 = fillet(ex11.edges().filter_by(Axis.Z), 5)
last = ex11.edges()
ex11 -= Hole(radius=width / 4, depth=thickness)
ex11 = fillet((ex11.edges() - last).sort_by().last, 2)

plane = Plane(ex11.faces().sort_by().last)
polygons = Sketch() + [
    plane * loc * RegularPolygon(radius=5, side_count=5)
    for loc in GridLocations(length / 2, width / 2, 2, 2)
]
ex11 -= extrude(polygons, -thickness)
# [Ex. 11]
# show_object(ex11)

##########################################
# 12. Defining an Edge with a Spline
# [Ex. 12]
pts = [
    (55, 30),
    (50, 35),
    (40, 30),
    (30, 20),
    (20, 25),
    (10, 20),
    (0, 20),
]

l1 = Spline(pts)
l2 = Line(l1 @ 0, (60, 0))
l3 = Line(l2 @ 1, (0, 0))
l4 = Line(l3 @ 1, l1 @ 1)

sk12 = make_face([l1, l2, l3, l4])
ex12 = extrude(sk12, 10)
# [Ex. 12]
# show_object(ex12)


##########################################
# 13. CounterBoreHoles, CounterSinkHoles and PolarLocations
# [Ex. 13]
a, b = 40, 4

ex13 = Cylinder(radius=50, height=10)
plane = Plane(ex13.faces().sort_by().last)

ex13 -= (
    plane
    * PolarLocations(radius=a, count=4)
    * CounterSinkHole(radius=b, counter_sink_radius=2 * b, depth=10)
)
ex13 -= (
    plane
    * PolarLocations(radius=a, count=4, start_angle=45, angular_range=360)
    * CounterBoreHole(
        radius=b, counter_bore_radius=2 * b, depth=10, counter_bore_depth=b
    )
)
# [Ex. 13]
# show_object(ex13)

##########################################
# 14. Position on a line with '@', '%' and introduce Sweep
# [Ex. 14]
a, b = 40, 20

l1 = JernArc(start=(0, 0), tangent=(0, 1), radius=a, arc_size=180)
l2 = JernArc(start=l1 @ 1, tangent=l1 % 1, radius=a, arc_size=-90)
l3 = Line(l2 @ 1, l2 @ 1 + (-a, a))
ex14_ln = l1 + l2 + l3

sk14 = Plane.XZ * Rectangle(b, b)
ex14 = sweep(sk14, path=ex14_ln)
# [Ex. 14]
# show_object(ex14)


##########################################
# 15. Mirroring Symmetric Geometry
# [Ex. 15]
a, b, c = 80, 40, 20

l1 = Line((0, 0), (a, 0))
l2 = Line(l1 @ 1, l1 @ 1 + (0, b))
l3 = Line(l2 @ 1, l2 @ 1 + (-c, 0))
l4 = Line(l3 @ 1, l3 @ 1 + (0, -c))
l5 = Line(l4 @ 1, (0, (l4 @ 1).Y))
ln = Curve() + [l1, l2, l3, l4, l5]
ln += mirror(ln, Plane.YZ)

sk15 = make_face(ln)
ex15 = extrude(sk15, c)
# [Ex. 15]
# show_object(ex15)

##########################################
# 16. Mirroring 3D Objects
# same concept as CQ docs, but different object
# [Ex. 16]
length, width, thickness = 80.0, 60.0, 10.0

sk16 = Rectangle(length, width)
sk16 = fillet(sk16.vertices(), length / 10)

circles = [loc * Circle(length / 12) for loc in GridLocations(length / 4, 0, 3, 1)]

sk16 = sk16 - circles - Rectangle(length, width, align=(Align.MIN, Align.MIN))
ex16_single = extrude(Plane.XZ * sk16, length)

planes = [
    Plane.XY.offset(width),
    Plane.YX.offset(width),
    Plane.YZ.offset(width),
    Plane.YZ.offset(-width),
]
objs = [mirror(ex16_single, plane) for plane in planes]
ex16 = ex16_single + objs
# [Ex. 16]
# show_object(ex16)

##########################################
# 17. Mirroring From Faces
# [Ex. 17]
a, b = 30, 20

sk17 = RegularPolygon(radius=a, side_count=5)
ex17 = extrude(sk17, amount=b)
ex17 += mirror(ex17, Plane(ex17.faces().sort_by(Axis.Y).first))
# [Ex. 17]
# show_object(ex17)

##########################################
# 18. Creating Workplanes on Faces
# based on Ex. 9
# [Ex. 18]
length, width, thickness = 80.0, 60.0, 10.0
a, b = 4, 5

ex18 = Part() + Box(length, width, thickness)
ex18 = chamfer(ex18.edges().group_by()[-1], a)
ex18 = fillet(ex18.edges().filter_by(Axis.Z), b)

sk18 = Plane(ex18.faces().sort_by().first) * Rectangle(2 * b, 2 * b)
ex18 -= extrude(sk18, -thickness)
# [Ex. 18]
# show_object(ex18)

##########################################
# 19. Locating a Workplane on a vertex
# [Ex. 19]
length, thickness = 80.0, 10.0

ex19_sk = RegularPolygon(radius=length / 2, side_count=7)
ex19 = extrude(ex19_sk, thickness)

topf = ex19.faces().sort_by().last

vtx = topf.vertices().group_by(Axis.X)[-1][0]

vtx2Axis = Axis((0, 0, 0), (-1, -0.5, 0))
vtx2 = topf.vertices().sort_by(vtx2Axis)[-1]

ex19_sk2 = Circle(radius=length / 8)
ex19_sk2 = Pos(vtx.X, vtx.Y) * ex19_sk2 + Pos(vtx2.X, vtx2.Y) * ex19_sk2

ex19 -= extrude(ex19_sk2, thickness)
# [Ex. 19]
# show_object(ex19)

##########################################
# 20. Offset Sketch Workplane
# [Ex. 20]
length, width, thickness = 80.0, 60.0, 10.0

ex20 = Box(length, width, thickness)
plane = Plane(ex20.faces().sort_by(Axis.X).first).offset(2 * thickness)

sk20 = plane * Circle(width / 3)
ex20 += extrude(sk20, width)
# [Ex. 20]
# show_object(ex20)

##########################################
# 21. Copying Workplanes
# [Ex. 21]
width, length = 10.0, 60.0

ex21 = extrude(Circle(width / 2), length)
plane = Plane(origin=ex21.center(), z_dir=(-1, 0, 0))
ex21 += plane * extrude(Circle(width / 2), length)
# [Ex. 21]
# show_object(ex21)

##########################################
# 22. Rotated Workplanes
# [Ex. 22]
length, width, thickness = 80.0, 60.0, 10.0

ex22 = Box(length, width, thickness)
plane = Plane((ex22.faces().group_by(Axis.Z)[0])[0]) * Rot(0, 50, 0)

holes = Sketch() + [
    plane * loc * Circle(thickness / 4)
    for loc in GridLocations(length / 4, width / 4, 2, 2)
]
ex22 -= extrude(holes, -100, both=True)
# [Ex. 22]
# show_object(ex22)

##########################################
# 23. Revolve
# [Ex. 23]
pts = [
    (-25, 35),
    (-25, 0),
    (-20, 0),
    (-20, 5),
    (-15, 10),
    (-15, 35),
]

l1 = Polyline(pts)
l2 = Line(l1 @ 1, l1 @ 0)
sk23 = make_face([l1, l2])

sk23 += Pos(0, 35) * Circle(25)
sk23 = Plane.XZ * split(sk23, bisect_by=Plane.ZY)

ex23 = revolve(sk23, Axis.Z)
# [Ex. 23]
# show_object(ex23)

##########################################
# 24. Lofts
# [Ex. 24]
length, width, thickness = 80.0, 60.0, 10.0

ex24 = Box(length, length, thickness)
plane = Plane(ex24.faces().sort_by().last)

faces = Sketch() + [
    plane * Circle(length / 3),
    plane.offset(length / 2) * Rectangle(length / 6, width / 6),
]

ex24 += loft(faces)
# [Ex. 24]
# show_object(ex24)

##########################################
# 25. Offset Sketch
# [Ex. 25]
rad, offs = 50, 10

sk25_1 = RegularPolygon(radius=rad, side_count=5)
sk25_2 = Plane.XY.offset(15) * RegularPolygon(radius=rad, side_count=5)
sk25_2 = offset(sk25_2, offs)
sk25_3 = Plane.XY.offset(30) * RegularPolygon(radius=rad, side_count=5)
sk25_3 = offset(sk25_3, offs, kind=Kind.INTERSECTION)

sk25 = Sketch() + [sk25_1, sk25_2, sk25_3]
ex25 = extrude(sk25, 1)
# [Ex. 25]
# show_object(ex25)

##########################################
# 26. Offset Part To Create Thin features
# [Ex. 26]
length, width, thickness, wall = 80.0, 60.0, 10.0, 2.0

ex26 = Box(length, width, thickness)
topf = ex26.faces().sort_by().last
ex26 = offset(ex26, amount=-wall, openings=topf)
# [Ex. 26]
# show_object(ex26)

##########################################
# 27. Splitting an Object
# [Ex. 27]
length, width, thickness = 80.0, 60.0, 10.0

ex27 = Box(length, width, thickness)
sk27 = Plane(ex27.faces().sort_by().first) * Circle(width / 4)
ex27 -= extrude(sk27, -thickness)
ex27 = split(ex27, Plane(ex27.faces().sort_by(Axis.Y).last).offset(-width / 2))
# [Ex. 27]
# show_object(ex27)

##########################################
# 28. Locating features based on Faces
# [Ex. 28]
width, thickness = 80.0, 10.0

sk28 = RegularPolygon(radius=width / 4, side_count=3)
tmp28 = extrude(sk28, thickness)
ex28 = Sphere(radius=width / 2)
for p in [Plane(face) for face in tmp28.faces().group_by(Axis.Z)[1]]:
    ex28 -= p * Hole(thickness / 2, depth=width)
# [Ex. 28]
# show_object(ex28)

##########################################
# 29. The Classic OCC Bottle
# [Ex. 29]
L, w, t, b, h, n = 60.0, 18.0, 9.0, 0.9, 90.0, 8.0

l1 = Line((0, 0), (0, w / 2))
l2 = ThreePointArc(l1 @ 1, (L / 2.0, w / 2.0 + t), (L, w / 2.0))
l3 = Line(l2 @ 1, ((l2 @ 1).X, 0, 0))
ln29 = l1 + l2 + l3
ln29 += mirror(ln29)
sk29 = make_face(ln29)
ex29 = extrude(sk29, -(h + b))
ex29 = fillet(ex29.edges(), radius=w / 6)

neck = Plane(ex29.faces().sort_by().last) * Circle(t)
ex29 += extrude(neck, n)
necktopf = ex29.faces().sort_by().last
ex29 = offset(ex29, -b, openings=necktopf)
# [Ex. 29]
# show_object(ex29)

##########################################
# 30. Bezier Curve
# [Ex. 30]
pts = [
    (0, 0),
    (20, 20),
    (40, 0),
    (0, -40),
    (-60, 0),
    (0, 100),
    (100, 0),
]

wts = [
    1.0,
    1.0,
    2.0,
    3.0,
    4.0,
    2.0,
    1.0,
]

ex30_ln = Polyline(pts) + Bezier(pts, weights=wts)
ex30_sk = make_face(ex30_ln)
ex30 = extrude(ex30_sk, -10)
# [Ex. 30]
# show_object(ex30)

##########################################
# 31. Nesting Locations
# [Ex. 31]
a, b, c = 80.0, 5.0, 3.0

ex31 = Rot(Z=30) * RegularPolygon(3 * b, 6)
ex31 += PolarLocations(a / 2, 6) * (
    RegularPolygon(b, 4) + GridLocations(3 * b, 3 * b, 2, 2) * RegularPolygon(b, 3)
)
ex31 = extrude(ex31, 3)
# [Ex. 31]
# show_object(ex31)

##########################################
# 32. Python for-loop
# [Ex. 32]
a, b, c = 80.0, 10.0, 1.0

ex32_sk = RegularPolygon(2 * b, 6, rotation=30)
ex32_sk += PolarLocations(a / 2, 6) * RegularPolygon(b, 4)
ex32 = Part() + [extrude(obj, c + 3 * idx) for idx, obj in enumerate(ex32_sk.faces())]
# [Ex. 32]
# show_object(ex32)

##########################################
# 33. Python function and for-loop
# [Ex. 33]
a, b, c = 80.0, 5.0, 1.0


def square(rad, loc):
    return loc * RegularPolygon(rad, 4)


ex33 = Part() + [
    extrude(square(b + 2 * i, loc), c + 2 * i)
    for i, loc in enumerate(PolarLocations(a / 2, 6))
]
# [Ex. 33]
# show_object(ex33)

##########################################
# 34. Embossed and Debossed Text
# [Ex. 34]
length, width, thickness, fontsz, fontht = 80.0, 60.0, 10.0, 25.0, 4.0

ex34 = Box(length, width, thickness)
plane = Plane(ex34.faces().sort_by().last)
ex34_sk = plane * Text("Hello", font_size=fontsz, align=(Align.CENTER, Align.MIN))
ex34 += extrude(ex34_sk, amount=fontht)
ex34_sk2 = plane * Text("World", font_size=fontsz, align=(Align.CENTER, Align.MAX))
ex34 -= extrude(ex34_sk2, amount=-fontht)
# [Ex. 34]
# show_object(ex34)

##########################################
# 35. Slots
# [Ex. 35]
length, width, thickness = 80.0, 60.0, 10.0

ex35 = Box(length, length, thickness)
plane = Plane(ex35.faces().sort_by().last)
ex35_sk = SlotCenterToCenter(width / 2, 10)
ex35_ln = RadiusArc((-width / 2, 0), (0, width / 2), radius=width / 2)
ex35_sk += SlotArc(arc=ex35_ln.edges()[0], height=thickness)
ex35_ln2 = RadiusArc((0, -width / 2), (width / 2, 0), radius=-width / 2)
ex35_sk += SlotArc(arc=ex35_ln2.edges()[0], height=thickness)
ex35 -= extrude(plane * ex35_sk, -thickness)
# [Ex. 35]
# show_object(ex35)

##########################################
# 36. Extrude-Until
# [Ex. 36]
rad, rev = 6, 50

ex36_sk = Pos(0, rev) * Circle(rad)
ex36 = revolve(axis=Axis.X, profiles=ex36_sk, revolution_arc=180)
ex36_sk2 = Rectangle(rad, rev)
ex36 += extrude(ex36_sk2, until=Until.NEXT, target=ex36)
# [Ex. 36]
# show_object(ex36)



================================================
FILE: docs/heart_token.py
================================================
# [Code]
from build123d import *
from ocp_vscode import show

# Create the edges of one half the heart surface
l1 = JernArc((0, 0), (1, 1.4), 40, -17)
l2 = JernArc(l1 @ 1, l1 % 1, 4.5, 175)
l3 = IntersectingLine(l2 @ 1, l2 % 1, other=Edge.make_line((0, 0), (0, 20)))
l4 = ThreePointArc(l3 @ 1, (0, 0, 1.5) + (l3 @ 1 + l1 @ 0) / 2, l1 @ 0)
heart_half = Wire([l1, l2, l3, l4])
# [SurfaceEdges]

# Create a point elevated off the center
surface_pnt = l2.arc_center + (0, 0, 1.5)
# [SurfacePoint]

# Create the surface from the edges and point
top_right_surface = Pos(Z=0.5) * -Face.make_surface(heart_half, [surface_pnt])
# [Surface]

# Use the mirror method to create the other top and bottom surfaces
top_left_surface = top_right_surface.mirror(Plane.YZ)
bottom_right_surface = top_right_surface.mirror(Plane.XY)
bottom_left_surface = -top_left_surface.mirror(Plane.XY)
# [Surfaces]

# Create the left and right sides
left_wire = Wire([l3, l2, l1])
left_side = Pos(Z=-0.5) * Shell.extrude(left_wire, (0, 0, 1))
right_side = left_side.mirror(Plane.YZ)
# [Sides]

# Put all of the faces together into a Shell/Solid
heart = Solid(
    Shell(
        [
            top_right_surface,
            top_left_surface,
            bottom_right_surface,
            bottom_left_surface,
            left_side,
            right_side,
        ]
    )
)
# [Solid]

# Build a frame around the heart
with BuildPart() as heart_token:
    with BuildSketch() as outline:
        with BuildLine():
            add(l1)
            add(l2)
            add(l3)
            Line(l3 @ 1, l1 @ 0)
        make_face()
        mirror(about=Plane.YZ)
        center = outline.sketch
        offset(amount=2, kind=Kind.INTERSECTION)
        add(center, mode=Mode.SUBTRACT)
    extrude(amount=2, both=True)
    add(heart)

heart_token.part.color = "Red"

show(heart_token)
# [End]
# export_gltf(heart_token.part, "heart_token.glb", binary=True)



================================================
FILE: docs/import_export.rst
================================================
#############
Import/Export
#############

Methods and functions specific to exporting and importing build123d objects are defined below.

For example:

.. code-block:: python

    with BuildPart() as box_builder:
        Box(1, 1, 1)
    export_step(box_builder.part, "box.step")

File Formats
============

3MF
---

The 3MF (3D Manufacturing Format) file format is a versatile and modern standard 
for representing 3D models used in additive manufacturing, 3D printing, and other 
applications. Developed by the 3MF Consortium, it aims to overcome the limitations 
of traditional 3D file formats by providing a more efficient and feature-rich solution. 
The 3MF format supports various advanced features like color information, texture mapping, 
multi-material definitions, and precise geometry representation, enabling seamless 
communication between design software, 3D printers, and other manufacturing devices. 
Its open and extensible nature makes it an ideal choice for exchanging complex 3D data 
in a compact and interoperable manner.

BREP
----

The BREP (Boundary Representation) file format is a widely used data format in 
computer-aided design (CAD) and computer-aided engineering (CAE) applications. 
BREP represents 3D geometry using topological entities like vertices, edges, 
and faces, along with their connectivity information. It provides a precise 
and comprehensive representation of complex 3D models, making it suitable for 
advanced modeling and analysis tasks. BREP files are widely supported by various 
CAD software, enabling seamless data exchange between different systems. Its ability 
to represent both geometric shapes and their topological relationships makes it a 
fundamental format for storing and sharing detailed 3D models.

DXF
---

The DXF (Drawing Exchange Format) file format is a widely used standard for 
representing 2D and 3D drawings, primarily used in computer-aided design (CAD) 
applications. Developed by Autodesk, DXF files store graphical and geometric data, 
such as lines, arcs, circles, and text, as well as information about layers, colors, 
and line weights. Due to its popularity, DXF files can be easily exchanged and 
shared between different CAD software. The format's simplicity and human-readable 
structure make it a versatile choice for sharing designs, drawings, and models 
across various CAD platforms, facilitating seamless collaboration in engineering 
and architectural projects.

glTF
----

The glTF (GL Transmission Format) is a royalty-free specification for the efficient 
transmission and loading of 3D models and scenes by applications. Developed by the 
Khronos Group, glTF is designed as a compact, interoperable format that enables the 
quick display of assets across various platforms and devices. glTF supports a rich 
feature set, including detailed meshes, materials, textures, skeletal animations, 
and more, facilitating complex 3D visualizations. It streamlines the process of 
sharing and deploying 3D content in web applications, game engines, and other 
visualization tools, making it the "JPEG of 3D." glTF's versatility and efficiency 
have led to its widespread adoption in the 3D content industry.

STL
---

The STL (STereoLithography) file format is a widely used file format in 3D printing 
and computer-aided design (CAD) applications. It represents 3D geometry using 
triangular facets to approximate the surface of a 3D model. STL files are widely 
supported and can store both the geometry and color information of the model. 
They are used for rapid prototyping and 3D printing, as they provide a simple and 
efficient way to represent complex 3D objects. The format's popularity stems from 
its ease of use, platform independence, and ability to accurately describe the 
surface of intricate 3D models with a minimal file size.

STEP
----

The STEP (Standard for the Exchange of Product model data) file format is a widely 
used standard for representing 3D product and manufacturing data in computer-aided 
design (CAD) and computer-aided engineering (CAE) applications. It is an ISO standard 
(ISO 10303) and supports the representation of complex 3D geometry, product structure, 
and metadata. STEP files store information in a neutral and standardized format, 
making them highly interoperable across different CAD/CAM software systems. They 
enable seamless data exchange between various engineering disciplines, facilitating 
collaboration and data integration throughout the entire product development and 
manufacturing process.

SVG
---

The SVG (Scalable Vector Graphics) file format is an XML-based standard used for 
describing 2D vector graphics. It is widely supported and can be displayed in modern 
web browsers, making it suitable for web-based graphics and interactive applications. 
SVG files define shapes, paths, text, and images using mathematical equations, 
allowing for smooth scalability without loss of quality. The format is ideal for 
logos, icons, illustrations, and other graphics that require resolution independence. 
SVG files are also easily editable in text editors or vector graphic software, making 
them a popular choice for designers and developers seeking flexible and versatile graphic 
representation.


2D Exporters 
============

Exports to DXF (Drawing Exchange Format) and SVG (Scalable Vector Graphics) 
are provided by the 2D Exporters: ExportDXF and ExportSVG classes. 

DXF is a widely used file format for exchanging CAD (Computer-Aided Design) 
data between different software applications. SVG is a widely used vector graphics
format that is supported by web browsers and various graphic editors.  

The core concept to these classes is the creation of a DXF/SVG document with 
specific properties followed by the addition of layers and shapes to the documents.
Once all of the layers and shapes have been added, the document can be written
to a file. 

3D to 2D Projection
-------------------

There are a couple ways to generate a 2D drawing of a 3D part:

* Generate a section: The  :func:`~operations_part.section` operation can be used to
  create a 2D cross section of a 3D part at a given plane.
* Generate a projection: The :meth:`~topology.Shape.project_to_viewport` method can be
  used to create a 2D projection of a 3D scene. Similar to a camera, the ``viewport_origin``
  defines the location of camera, the ``viewport_up`` defines the orientation of the camera,
  and the ``look_at`` parameter defined where the camera is pointed.  By default, 
  ``viewport_up`` is the positive z axis and ``look_up`` is the center of the shape.  The
  return value is a tuple of lists of edges, the first the visible edges and the second
  the hidden edges.  
  
Each of these Edges and Faces can be assigned different line color/types and fill colors
as described below (as ``project_to_viewport`` only generates Edges, fill doesn't apply).  
The shapes generated from the above steps are to be added as shapes 
in one of the exporters described below and written as either a DXF or SVG file as shown
in this example:

.. code-block:: python

    view_port_origin=(-100, -50, 30)
    visible, hidden = part.project_to_viewport(view_port_origin)
    max_dimension = max(*Compound(children=visible + hidden).bounding_box().size)
    exporter = ExportSVG(scale=100 / max_dimension)
    exporter.add_layer("Visible")
    exporter.add_layer("Hidden", line_color=(99, 99, 99), line_type=LineType.ISO_DOT)
    exporter.add_shape(visible, layer="Visible")
    exporter.add_shape(hidden, layer="Hidden")
    exporter.write("part_projection.svg")

LineType
--------

ANSI (American National Standards Institute) and ISO (International Organization for 
Standardization) standards both define line types in drawings used in DXF and SVG
exported drawings:

* ANSI Standards:
   * ANSI/ASME Y14.2 - "Line Conventions and Lettering" is the standard that defines 
     line types, line weights, and line usage in engineering drawings in the United States.

* ISO Standards:
   * ISO 128 - "Technical drawings -- General principles of presentation" is the ISO 
     standard that covers the general principles of technical drawing presentation, 
     including line types and line conventions.
   * ISO 13567 - "Technical product documentation (TPD) -- Organization and naming of 
     layers for CAD" provides guidelines for the organization and naming of layers in 
     Computer-Aided Design (CAD) systems, which may include line type information.

These standards help ensure consistency and clarity in technical drawings, making it 
easier for engineers, designers, and manufacturers to communicate and interpret the 
information presented in the drawings.

The line types used by the 2D Exporters are defined by the :class:`~exporters.LineType` 
Enum and are shown in the following diagram:

.. image:: assets/line_types.svg
    :align: center


ExportDXF
---------

.. autoclass:: exporters.ExportDXF
    :noindex:

ExportSVG
---------

.. autoclass:: exporters.ExportSVG
    :noindex:

3D Exporters
============

.. py:module:: exporters3d

.. autofunction:: export_brep
   :noindex:

.. autofunction:: export_gltf
   :noindex:

.. autofunction:: export_step
   :noindex:

.. autofunction:: export_stl
   :noindex:

3D Mesh Export
--------------

Both 3MF and STL export (and import) are provided with the :class:`~mesher.Mesher` class.
As mentioned above, the 3MF format it provides is feature-rich and therefore has a slightly
more complex API than the simple Shape exporters.

For example:

.. code-block:: python

    # Create the shapes and assign attributes
    blue_shape = Solid.make_cone(20, 0, 50)
    blue_shape.color = Color("blue")
    blue_shape.label = "blue"
    blue_uuid = uuid.uuid1()
    red_shape = Solid.make_cylinder(5, 50).move(Location((0, -30, 0)))
    red_shape.color = Color("red")
    red_shape.label = "red"

    # Create a Mesher instance as an exporter, add shapes and write
    exporter = Mesher()
    exporter.add_shape(blue_shape, part_number="blue-1234-5", uuid_value=blue_uuid)
    exporter.add_shape(red_shape)
    exporter.add_meta_data(
        name_space="custom",
        name="test_meta_data",
        value="hello world",
        metadata_type="str",
        must_preserve=False,
    )
    exporter.add_code_to_metadata()
    exporter.write("example.3mf")
    exporter.write("example.stl")

.. autoclass:: mesher.Mesher

.. note::

    If you need to align multiple components for 3D printing, you can use the  :ref:`pack() <pack>` function to arrange the objects side by side and align them on the same plane. This ensures that your components are well-organized and ready for the printing process.


2D Importers
============
.. py:module:: importers

.. autofunction:: import_svg
.. autofunction:: import_svg_as_buildline_code

3D Importers
============

.. autofunction:: import_brep
.. autofunction:: import_step
.. autofunction:: import_stl

3D Mesh Import
--------------

Both 3MF and STL import (and export) are provided with the :class:`~mesher.Mesher` class.

For example:

.. code-block:: python

    importer = Mesher()
    cone, cyl = importer.read("example.3mf")
    print(
        f"{importer.mesh_count=}, {importer.vertex_counts=}, {importer.triangle_counts=}"
    )
    print(f"Imported model unit: {importer.model_unit}")
    print(f"{cone.label=}")
    print(f"{cone.color.to_tuple()=}")
    print(f"{cyl.label=}")
    print(f"{cyl.color.to_tuple()=}")

.. code-block:: none

    importer.mesh_count=2, importer.vertex_counts=[66, 52], importer.triangle_counts=[128, 100]
    Imported model unit: Unit.MM
    cone.label='blue'
    cone.color.to_tuple()=(0.0, 0.0, 1.0, 1.0)
    cyl.label='red'
    cyl.color.to_tuple()=(1.0, 0.0, 0.0, 1.0)



================================================
FILE: docs/index.rst
================================================
..
    build123d readthedocs documentation

    by:   Gumyr
    date: July 13th 2022

    desc: This is the documentation for build123d on readthedocs

    license:

        Copyright 2022 Gumyr

        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at

            http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.


.. highlight:: python

.. image:: ./assets/build123d_logo/logo-banner.svg
  :align: center
  :alt: build123d logo

########
About
########

Build123d is a Python-based, parametric (BREP) modeling framework for 2D and 3D CAD. 
Built on the Open Cascade geometric kernel, it provides a clean, fully Pythonic interface 
for creating precise models suitable for 3D printing, CNC machining, laser cutting, and 
other manufacturing processes. Models can be exported to popular CAD tools such as FreeCAD 
and SolidWorks.

Designed for modern, maintainable CAD-as-code, build123d combines clear architecture with 
expressive, algebraic modeling. It offers:

* Minimal or no internal state depending on mode
* Explicit 1D, 2D, and 3D geometry classes with well-defined operations
* Extensibility through subclassing and functional composition—no monkey patching
* Standards-compliant code (PEP 8, mypy, pylint) with rich pylance type hints
* Deep Python integration—selectors as lists, locations as iterables, and natural 
  conversions (``Solid(shell)``, ``tuple(Vector)``)
* Operator-driven modeling (``obj += sub_obj``, ``Plane.XZ * Pos(X=5) * Rectangle(1, 1)``) 
  for algebraic, readable, and composable design logic

The result is a framework that feels native to Python while providing the full power of 
OpenCascade geometry underneath.


With build123d, intricate parametric models can be created in just a few lines of readable 
Python code—as demonstrated by the tea cup example below.

.. dropdown:: Teacup Example

  .. literalinclude:: ../examples/tea_cup.py
      :start-after: [Code]
      :end-before: [End]

.. raw:: html

    <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <model-viewer poster="_images/tea_cup.png" src="_static/tea_cup.glb" alt="A tea cup modelled in build123d" auto-rotate camera-controls style="width: 100%; height: 50vh;"></model-viewer>

.. note::


  This documentation is available in
  `pdf <https://build123d.readthedocs.io/_/downloads/en/latest/pdf/>`_ and
  `epub <https://build123d.readthedocs.io/_/downloads/en/latest/epub/>`_ formats
  for reference while offline.

.. note::

  There is a `Discord <https://discord.com/invite/Bj9AQPsCfx>`_ server (shared with CadQuery) where
  you can ask for help in the build123d channel.

#################
Table Of Contents
#################

.. toctree::
    :maxdepth: 2

    introduction.rst
    installation.rst
    key_concepts.rst
    key_concepts_builder.rst
    key_concepts_algebra.rst
    moving_objects.rst
    OpenSCAD.rst
    introductory_examples.rst
    tutorials.rst
    objects.rst
    operations.rst
    topology_selection.rst
    builders.rst
    joints.rst
    assemblies.rst
    tips.rst
    import_export.rst
    advanced.rst
    cheat_sheet.rst
    external.rst
    builder_api_reference.rst
    direct_api_reference.rst

==================
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



================================================
FILE: docs/installation.rst
================================================
############
Installation
############

The recommended method for most users to install **build123d** is:

.. doctest::

	>>> pip install build123d

.. note::

	The `ocp-vscode <https://github.com/bernhard-42/vscode-ocp-cad-viewer>`_ viewer has
	the ability to install **build123d**.

Install build123d from GitHub:
------------------------------

To get the latest non-released version of **build123d** one can install from GitHub using one of the following two commands:

In Linux/MacOS, use the following command:

.. doctest::

	>>> python3 -m pip install git+https://github.com/gumyr/build123d

In Windows, use the following command:

.. doctest::

	>>> python -m pip install git+https://github.com/gumyr/build123d

If you receive errors about conflicting dependencies, you can retry the installation after having
upgraded pip to the latest version with the following command:

.. doctest::

	>>> python3 -m pip install --upgrade pip

If you use `poetry <https://python-poetry.org/>`_ to install build123d, you can simply use:

.. doctest::

	>>> poetry add build123d

However, if you want the latest commit from GitHub you might need to specify
the branch that is used for git-based installs; until quite recently, poetry used to checkout the
`master` branch when none was specified, and this fails on build123d that uses a `dev` branch.

Pip does not suffer from this issue because it correctly fetches the repository default branch.

If you are a poetry user, you can work around this issue by installing build123d in the following
way:

.. doctest::

	>>> poetry add git+https://github.com/gumyr/build123d.git@dev

Please note that always suffixing the URL with ``@dev`` is safe and will work with both older and
recent versions of poetry.

Development install of build123d:
----------------------------------------------
**Warning**: it is highly recommended to upgrade pip to the latest version before installing
build123d, especially in development mode. This can be done with the following command:

.. doctest::

	>>> python3 -m pip install --upgrade pip

Once pip is up-to-date, you can install build123d
`in development mode <https://setuptools.pypa.io/en/latest/userguide/development_mode.html>`_
with the following commands:

.. doctest::

	>>> git clone https://github.com/gumyr/build123d.git
	>>> cd build123d
	>>> python3 -m pip install -e .

Please substitute ``python3`` with ``python`` in the lines above if you are using Windows.

If you're working directly with the OpenCascade ``OCP`` layer you will likely want to install
the OCP stubs as follows:

.. doctest::

	>>> python3 -m pip install git+https://github.com/CadQuery/OCP-stubs@7.7.0

Test your build123d installation:
----------------------------------------------
If all has gone well, you can open a command line/prompt, and type:

.. doctest::

	>>> python
	>>> from build123d import *
	>>> print(Solid.make_box(1,2,3).show_topology(limit_class="Face"))

Which should return something similar to:

.. code::

		Solid        at 0x165e75379f0, Center(0.5, 1.0, 1.5)
		└── Shell    at 0x165eab056f0, Center(0.5, 1.0, 1.5)
			├── Face at 0x165b35a3570, Center(0.0, 1.0, 1.5)
			├── Face at 0x165e77957f0, Center(1.0, 1.0, 1.5)
			├── Face at 0x165b3e730f0, Center(0.5, 0.0, 1.5)
			├── Face at 0x165e8821570, Center(0.5, 2.0, 1.5)
			├── Face at 0x165e88218f0, Center(0.5, 1.0, 0.0)
			└── Face at 0x165eb21ee70, Center(0.5, 1.0, 3.0)

Adding a nicer GUI
----------------------------------------------

If you prefer to have a GUI available, your best option is to choose one from here: :ref:`external`



================================================
FILE: docs/introduction.rst
================================================
############
Introduction
############

***********
Key Aspects
***********

The following sections describe some of the key aspects of build123d and illustrate
why one might choose this open source system over proprietary options like SolidWorks,
OnShape, Fusion 360, or even other open source systems like Blender, or OpenSCAD.

Boundary Representation (BREP) Modelling
========================================

Boundary representation (BREP) and mesh-based CAD systems are both used to
create and manipulate 3D models, but they differ in the way they represent and
store the models.

Advantages of BREP-based CAD systems (e.g. build123d & SolidWorks):

* Precision: BREP-based CAD systems use mathematical representations to define
  the shape of an object, which allows for more precise and accurate modeling of
  complex shapes.
* Topology: BREP-based CAD systems maintain topological information of the 3D
  model, such as edges, faces and vertices. This allows for more robust and stable
  modeling, such as Boolean operations.
* Analytical modeling: BREP-based CAD systems can take advantage of the
  topological information to perform analytical operations such as collision
  detection, mass properties calculations, and finite element analysis.
* Features-based modeling: BREP-based CAD systems are often feature-based, which
  means that the model is built by creating and modifying individual features,
  such as holes, fillets, and chamfers. This allows for parametric design and easy
  modification of the model.
* Efficient storage: BREP-based CAD systems use a compact representation to
  store the 3D model, which is more efficient than storing a large number of
  triangles used in mesh-based systems.


Advantages of Mesh-based CAD systems (e.g. Blender, OpenSCAD):

* Simplicity: Mesh-based CAD systems use a large number of triangles to
  represent the surface of an object, which makes them easy to use and understand.
* Real-time rendering: Mesh-based CAD systems can be rendered in real-time,
  which is useful for applications such as video games and virtual reality.
* Flexibility: Mesh-based CAD systems can be easily exported to other 3D
  modeling and animation software, which makes them a good choice for use in the
  entertainment industry.
* Handling of freeform surfaces: Mesh-based systems are better equipped to
  handle freeform surfaces, such as those found in organic shapes, as they do not
  rely on mathematical representation.
* Handling of large datasets: Mesh-based systems are more suitable for handling
  large datasets such as point clouds, as they can be easily converted into a mesh
  representation.

Parameterized Models
====================

Parametrized CAD systems are more effective than non-parametric CAD systems in
several ways:

* Reusability: Parametrized CAD models can be easily modified by changing a set
  of parameters, such as the length or width of an object, rather than having to
  manually edit the geometry. This makes it easy to create variations of a design
  without having to start from scratch.
* Design exploration: Parametrized CAD systems allow for easy exploration of
  different design options by changing the parameters and quickly visualizing the
  results.  This can save a lot of time and effort during the design process.
* Constraints and relationships: Parametrized CAD systems allow for the
  definition of constraints and relationships between different parameters. This
  ensures that the model remains valid and functional even when parameters are
  changed.
* Automation: Parametrized CAD systems can be automated to perform repetitive
  tasks, such as generating detailed drawings or creating parts lists. This can
  save a lot of time and effort and reduce the risk of errors.
* Collaboration: Parametrized CAD systems allow different team members to work
  on different aspects of a design simultaneously and ensure that the model
  remains consistent across different stages of the development process.
* Document management: Parametrized CAD systems can generate engineering
  drawings, BOMs, and other documents automatically, which makes it easier to
  manage and track the design history.

In summary, parametrized CAD systems are more effective than non-parametric CAD
systems because they provide a more efficient and flexible way to create and
modify designs, and can be easily integrated into the design, manufacturing, and
documentation process.

Python Programming Language
===========================

Python is a popular, high-level programming language that has several advantages
over other programming languages:

* Readability: Python code is easy to read and understand, with a clear and
  consistent syntax. This makes it a great language for beginners and for teams of
  developers who need to collaborate on a project.
* Versatility: Python is a general-purpose language that can be used for a wide
  range of tasks, including web development, scientific computing, data analysis,
  artificial intelligence, and more. This makes it a great choice for developers
  who need to work on multiple types of projects.
* Large community: Python has a large and active community of developers who
  contribute to the language and its ecosystem. This means that there are many
  libraries and frameworks available for developers to use, which can save a lot
  of time and effort.
* Good for data science, machine learning, and CAD: Python has a number of libraries
  such as numpy, pandas, scikit-learn, tensorflow, and cadquery which are popularly
  used in data science and machine learning and CAD.
* High-level language: Python is a high-level language, which means it abstracts
  away many of the low-level details of the computer.  This makes it easy to write
  code quickly and focus on solving the problem at hand.
* Cross-platform: Python code runs on many different platforms, including
  Windows, Mac, and Linux, making it a great choice for developers who need to
  write code that runs on multiple operating systems.
* Open-source: Python is an open-source programming language, which means it is
  free to use and distribute.  This makes it accessible to developers of all
  levels and budgets.
* Large number of libraries and modules: Python has a vast collection of
  libraries and modules that make it easy to accomplish complex tasks such as
  connecting to web servers, reading and modifying files, and connecting to
  databases.

Open Source Software
====================

Open source and proprietary software systems are different in several ways: B
Licensing: Open source software is licensed in a way that allows users to view,
modify, and distribute the source code, while proprietary software is closed
source and the source code is not available to the public.

* Ownership: Open source software is usually developed and maintained by a
  community of developers, while proprietary software is owned by a company or
  individual.
* Cost: Open source software is typically free to use, while proprietary
  software may require payment for a license or subscription.  Customization: Open
  source software can be modified and customized by users and developers, while
  proprietary software is typically not modifiable by users.
* Support: Open source software may have a larger community of users who can
  provide support, while proprietary software may have a smaller community and
  relies on the company for support.  Security: Open source software can be
  audited by a large community of developers, which can make it more secure, while
  proprietary software may have fewer eyes on the code and may be more vulnerable
  to security issues.
* Interoperability: Open source software may have better interoperability with
  other software and platforms, while proprietary software may have more limited
  compatibility.
* Reliability: Open source software can be considered as reliable as proprietary
  software. It is usually used by large companies, governments, and organizations
  and has been tested by a large number of users.

In summary, open source and proprietary software systems are different in terms
of licensing, ownership, cost, customization, support, security,
interoperability, and reliability. Open source software is typically free to use
and can be modified by users and developers, while proprietary software is
closed-source and may require payment for a license or subscription. Open source
software may have a larger community of users who can provide support, while
proprietary software may have a smaller community and relies on the company for
support.

Source Code Control Systems
===========================

Most GUI based CAD systems provide version control systems which represent the
CAD design and its history. They allows developers to see changes made to the design
over time, in a format that is easy to understand.

On the other hand, a source code control system like Git, is a command-line tool
and it provides more granular control over the code. This makes it suitable for
more advanced users and developers who are comfortable working with command-line
interfaces. A source code control system like Git is more flexible and allows
developers to perform tasks like branching and merging, which are not easily
done with a GUI version control system. Systems like Git have several advantages,
including:

* Version control: Git allows developers to keep track of changes made to the
  code over time, making it easy to revert to a previous version if necessary.
* Collaboration: Git makes it easy for multiple developers to work on the same
  codebase simultaneously, with the ability to merge changes from different
  branches of development.
* Backup: Git provides a way to backup and store the codebase in a remote
  repository, like GitHub. This can serve as a disaster recovery mechanism, in
  case of data loss.
* Branching: Git allows developers to create multiple branches of a project for
  different features or bug fixes, which can be easily merged into the main
  codebase once they are complete.
* Auditing: Git allows you to see who made changes to the code, when and what
  changes were made, which is useful for auditing and debugging.
* Open-source development: Git makes it easy for open-source developers to
  contribute to a project and share their work with the community.
* Flexibility: Git is a distributed version control system, which means that
  developers can work independently and offline.  They can then push their changes
  to a remote repository when they are ready to share them with others.

In summary, GUI version control systems are generally more user-friendly and
easier to use, while source code control systems like Git offer more flexibility
and control over the code. Both can be used to achieve the same goal, but they
cater to different types of users and use cases.

Automated Testing
=================

Users of source based CAD systems can benefit from automated testing which improves
their source code by:

* Finding bugs: Automated tests can detect bugs in the code, which can then be
  fixed before the code is released.  This helps to ensure that the code is of
  higher quality and less likely to cause issues when used.
* Regression testing: Automated tests can be used to detect regressions, which
  are bugs that are introduced by changes to the codebase. This helps to ensure
  that changes to the code do not break existing functionality.
* Documenting code behavior: Automated tests can serve as documentation for how
  the code is supposed to behave. This makes it easier for developers to
  understand the code and make changes without breaking it.
* Improving code design: Writing automated tests often requires a good
  understanding of the code and how it is supposed to behave. This can lead to a
  better design of the code, as developers will have a better understanding of the
  requirements and constraints.
* Saving time and cost: Automated testing can save time and cost by reducing the
  need for manual testing. Automated tests can be run quickly and often, which
  means that bugs can be found and fixed early in the development process, which
  is less expensive than finding them later.
* Continuous integration and delivery: Automated testing can be integrated into
  a continuous integration and delivery (CI/CD) pipeline. This means that tests
  are run automatically every time code is committed and can be integrated with
  other tools such as code coverage, static analysis and more.
* Improving maintainability: Automated tests can improve the maintainability of
  the code by making it easier to refactor and change the codebase. This is
  because automated tests provide a safety net that ensures that changes to the
  code do not introduce new bugs.

Overall, automated testing is an essential part of the software development
process, it helps to improve the quality of the code by detecting bugs early,
documenting code behavior, and reducing the cost of maintaining and updating the
code.

Automated Documentation
=======================

The Sphinx automated documentation system was used to create the page you are
reading now and can be used for user design documentation as well.  Such systems
are used for several reasons:

* Consistency: Sphinx and other automated documentation systems can generate
  documentation in a consistent format and style, which makes it easier to
  understand and use.
* Automation: Sphinx can automatically generate documentation from source code
  and comments, which saves time and effort compared to manually writing
  documentation.
* Up-to-date documentation: Automated documentation systems like Sphinx can
  update the documentation automatically when the code changes, ensuring that the
  documentation stays up-to-date with the code.
* Searchability: Sphinx and other automated documentation systems can include
  search functionality, which makes it easy to find the information you need.
* Cross-referencing: Sphinx can automatically create links between different
  parts of the documentation, making it easy to navigate and understand the
  relationships between different parts of the code.
* Customizable: Sphinx and other automated documentation systems can be
  customized to match the look and feel of your company's documentation.
* Multiple output formats: Sphinx can generate documentation in multiple formats
  such as HTML, PDF, ePub, and more.
* Support for multiple languages: Sphinx can generate documentation in multiple
  languages, which can make it easier to support international users.
* Integration with code management: Sphinx can be integrated with code
  management tools like Git, which allows documentation to be versioned along with
  the code.

In summary, automated documentation systems like Sphinx are used to generate
consistent, up-to-date, and searchable documentation from source code and
comments. They save time and effort compared to manual documentation, and can be
customized to match the look and feel of your company's documentation. They also
provide multiple output formats, support for multiple languages and can be
integrated with code management tools.


************************
Advantages Over CadQuery
************************

.. include:: advantages.rst



================================================
FILE: docs/introductory_examples.rst
================================================
#########################
Introductory Examples
#########################

The examples on this page can help you learn how to build objects with build123d, and are intended as a general overview of build123d.

They are organized from simple to complex, so working through them in order is the best way to absorb them.

.. note::

    Some important lines are omitted below to save space, so you will most likely need to add 1 & 2 to the provided code below for them to work:

       1. ``from build123d import *``
       2. If you are using build123d *builder mode* or *algebra mode*,

            - in *ocp_vscode* simply use e.g. ``show(ex15)`` to the end of your design to view parts, sketches and curves. ``show_all()`` can be used to automatically show all objects with their variable names as labels.
            - in *CQ-editor* add e.g. ``show_object(ex15.part)``, ``show_object(ex15.sketch)`` or ``show_object(ex15.line)`` to the end of your design to view parts, sketches or lines.

       3. If you want to save your resulting object as an STL from *builder mode*, you can use e.g. ``export_stl(ex15.part, "file.stl")``.
       4. If you want to save your resulting object as an STL from *algebra mode*, you can use e.g. ``export_stl(ex15, "file.stl")``
       5. build123d also supports exporting to multiple other file formats including STEP, see here for further information: `Import/Export Formats <https://build123d.readthedocs.io/en/latest/import_export.html>`_

.. contents:: List of Examples
    :backlinks: entry

.. _ex 1:

1. Simple Rectangular Plate
---------------------------------------------------

Just about the simplest possible example, a rectangular :class:`~objects_part.Box`.

.. image:: assets/general_ex1.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 1]
        :end-before: [Ex. 1]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 1]
        :end-before: [Ex. 1]


.. _ex 2:

2. Plate with Hole
---------------------------------------------------

A rectangular box, but with a hole added.

.. image:: assets/general_ex2.svg
    :align: center

* **Builder mode**

    In this case we are using
    :class:`~build_enums.Mode` ``.SUBTRACT`` to cut the :class:`~objects_part.Cylinder`
    from the :class:`~objects_part.Box`.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 2]
        :end-before: [Ex. 2]

* **Algebra mode**

    In this case we are using
    the subtract operator ``-`` to cut the :class:`~objects_part.Cylinder`
    from the :class:`~objects_part.Box`.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 2]
        :end-before: [Ex. 2]


.. _ex 3:

3. An extruded prismatic solid
---------------------------------------------------

Build a prismatic solid using extrusion.

.. image:: assets/general_ex3.svg
    :align: center

* **Builder mode**

    This time we can first create a 2D :class:`~build_sketch.BuildSketch` adding a
    :class:`~objects_sketch.Circle` and a subtracted :class:`~objects_sketch.Rectangle``
    and then use :class:`~build_part.BuildPart`'s :meth:`~operations_part.extrude` feature.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 3]
        :end-before: [Ex. 3]

* **Algebra mode**

    This time we can first create a 2D :class:`~objects_sketch.Circle` with a subtracted
    :class:`~objects_sketch.Rectangle`` and then use the :meth:`~operations_part.extrude` operation for parts.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 3]
        :end-before: [Ex. 3]


.. _ex 4:

4. Building Profiles using lines and arcs
---------------------------------------------------

Sometimes you need to build complex profiles using lines and arcs. This example
builds a prismatic solid from 2D operations. It is not necessary to create
variables for the line segments, but it will be useful in a later example.

.. image:: assets/general_ex4.svg
    :align: center

* **Builder mode**

    :class:`~build_sketch.BuildSketch` operates on closed Faces, and the operation
    :meth:`~operations_sketch.make_face` is used to convert the pending line segments
    from :class:`~build_line.BuildLine` into a closed Face.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 4]
        :end-before: [Ex. 4]

* **Algebra mode**

    We start with an empty :class:`~topology.Curve` and add lines to it (note that
    ``Curve() + [line1, line2, line3]`` is much more efficient than ``line1 + line2 + line3``,
    see :ref:`algebra_performance`).
    The operation :meth:`~operations_sketch.make_face` is used to convert the line
    segments into a Face.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 4]
        :end-before: [Ex. 4]

Note that to build a closed face it requires line segments that form a closed shape.

.. _ex 5:

5. Moving the current working point
---------------------------------------------------


.. image:: assets/general_ex5.svg
    :align: center

* **Builder mode**

    Using :class:`~build_common.Locations` we can place one (or multiple) objects
    at one (or multiple) places.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 5]
        :end-before: [Ex. 5]

* **Algebra mode**

    Using the pattern ``Pos(x, y, z=0) * obj`` (with :class:`geometry.Pos`) we can move an
    object to the provided position. Using ``Rot(x_angle, y_angle, z_angle) * obj``
    (with :class:`geometry.Rot`)  would rotate the object.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 5]
        :end-before: [Ex. 5]


.. _ex 6:

6. Using Point Lists
---------------------------------------------------

Sometimes you need to create a number of features at various
:class:`~build_common.Locations`.

.. image:: assets/general_ex6.svg
    :align: center

* **Builder mode**

    You can use a list of points to construct multiple objects at once.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 6]
        :end-before: [Ex. 6]

* **Algebra mode**

    You can use loops to iterate over these Locations
    or list comprehensions as in the example.

    The algebra operations are vectorized, which means ``obj - [obj1, obj2, obj3]``
    is short for ``obj - obj1 - obj2 - ob3`` (and more efficient, see :ref:`algebra_performance`).

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 6]
        :end-before: [Ex. 6]


.. _ex 7:

7. Polygons
---------------------------------------------------

.. image:: assets/general_ex7.svg
    :align: center

* **Builder mode**

    You can create :class:`~objects_sketch.RegularPolygon` for each stack point if
    you would like.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 7]
        :end-before: [Ex. 7]

* **Algebra mode**

    You can apply locations to :class:`~objects_sketch.RegularPolygon` instances
    for each location  via loops or list comprehensions.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 7]
        :end-before: [Ex. 7]


.. _ex 8:

8. Polylines
---------------------------------------------------

:class:`~objects_curve.Polyline` allows creating a shape from a large number
of chained points connected by lines. This example uses a polyline to create
one half of an i-beam shape, which is :meth:`~operations_generic.mirror` ed to
create the final profile.

.. image:: assets/general_ex8.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 8]
        :end-before: [Ex. 8]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 8]
        :end-before: [Ex. 8]


.. _ex 9:

9. Selectors, Fillets, and Chamfers
---------------------------------------------------

This example introduces multiple useful and important concepts. Firstly :meth:`~operations_generic.chamfer`
and :meth:`~operations_generic.fillet` can be used to "bevel" and "round" edges respectively. Secondly,
these two methods require an edge or a list of edges to operate on. To select all
edges, you could simply pass in ``ex9.edges()``.

.. image:: assets/general_ex9.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 9]
        :end-before: [Ex. 9]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 9]
        :end-before: [Ex. 9]

Note that :meth:`~topology.ShapeList.group_by` ``(Axis.Z)`` returns a list of lists of edges that is grouped by
their z-position. In this case we want to use the ``[-1]`` group which, by convention, will
be the highest z-dimension group.


.. _ex 10:

10. Select Last and Hole
---------------------------------------------------


.. image:: assets/general_ex10.svg
    :align: center

* **Builder mode**

    Using :class:`~build_enums.Select` ``.LAST`` you can select the most recently modified edges.
    It is used to perform a :meth:`~operations_generic.fillet` in this example. This example also
    makes use of :class:`~objects_part.Hole` which automatically cuts through the entire part.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 10]
        :end-before: [Ex. 10]

* **Algebra mode**

    Using the pattern ``snapshot = obj.edges()`` before and ``last_edges = obj.edges() - snapshot`` after an
    operation allows to select the most recently modified edges (same for ``faces``, ``vertices``, ...).
    It is used to perform a :meth:`~operations_generic.fillet` in this example. This example also makes use
    of :class:`~objects_part.Hole`. Different to the *context mode*, you have to add the ``depth`` of the whole.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 10]
        :end-before: [Ex. 10]


.. _ex 11:

11. Use a face as a plane for BuildSketch and introduce GridLocations
----------------------------------------------------------------------------


.. image:: assets/general_ex11.svg
    :align: center

* **Builder mode**

    :class:`~build_sketch.BuildSketch` accepts a Plane or a Face, so in this case we locate the Sketch
    on the top of the part. Note that the face used as input to BuildSketch needs
    to be Planar or unpredictable behavior can result. Additionally :class:`~build_common.GridLocations`
    can be used to create a grid of points that are simultaneously used to place 4
    pentagons.

    Lastly, :meth:`~operations_part.extrude` can be used with a negative amount and ``Mode.SUBTRACT`` to
    cut these from the parent.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 11]
        :end-before: [Ex. 11]

* **Algebra mode**

    The pattern ``plane * obj`` can be used to locate an object on a plane. Furthermore, the pattern
    ``plane * location * obj`` first places the object on a plane and then moves it relative to plane
    according to ``location``.

    :class:`~build_common.GridLocations` creates a grid of points that can be used in loops or list
    comprehensions as described earlier.

    Lastly, :meth:`~operations_part.extrude` can be used with a negative amount and cut (``-``) from the
    parent.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 11]
        :end-before: [Ex. 11]

Note that the direction implied by positive or negative inputs to amount is relative to the
normal direction of the face or plane. As a result of this, unexpected behavior can occur
if the extrude direction and mode/operation (ADD / ``+`` or SUBTRACT / ``-``) are not correctly set.

.. _ex 12:

12. Defining an Edge with a Spline
---------------------------------------------------

This example defines a side using a spline curve through a collection of points. Useful when you have an
edge that needs a complex profile.

.. image:: assets/general_ex12.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 12]
        :end-before: [Ex. 12]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 12]
        :end-before: [Ex. 12]


.. _ex 13:

13. CounterBoreHoles, CounterSinkHoles and PolarLocations
-------------------------------------------------------------

Counter-sink and counter-bore holes are useful for creating recessed areas for fasteners.

.. image:: assets/general_ex13.svg
    :align: center

* **Builder mode**

    We use a face to establish a location for :class:`~build_common.Locations`.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 13]
        :end-before: [Ex. 13]

* **Algebra mode**

    We use a face to establish a plane that is used later in the code for locating objects
    onto this plane.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 13]
        :end-before: [Ex. 13]

:class:`~build_common.PolarLocations` creates a list of points that are radially distributed.

.. _ex 14:

14. Position on a line with '\@', '\%' and introduce Sweep
------------------------------------------------------------

build123d includes a feature for finding the position along a line segment. This
is normalized between 0 and 1 and can be accessed using the :meth:`~topology.Mixin1D.position_at` (`@`) operator.
Similarly the :meth:`~topology.Mixin1D.tangent_at` (`%`) operator returns the line direction at a given point.

These two features are very powerful for chaining line segments together without
having to repeat dimensions again and again, which is error prone, time
consuming, and more difficult to maintain. The pending faces must lie on the
path, please see example 37 for a way to make this placement easier.


.. image:: assets/general_ex14.svg
    :align: center

* **Builder mode**

    The :meth:`~operations_generic.sweep` method takes any pending faces and sweeps them through the provided
    path (in this case the path is taken from the pending edges from ``ex14_ln``).
    :meth:`~operations_part.revolve` requires a single connected wire. 

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 14]
        :end-before: [Ex. 14]

* **Algebra mode**

    The :meth:`~operations_generic.sweep` method takes any faces and sweeps them through the provided
    path (in this case the path is taken from ``ex14_ln``).

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 14]
        :end-before: [Ex. 14]

It is also possible to use tuple or :class:`~geometry.Vector` addition (and other vector math operations)
as seen in the ``l3`` variable.

.. _ex 15:

15. Mirroring Symmetric Geometry
---------------------------------------------------

Here mirror is used on the BuildLine to create a symmetric shape with fewer line segment commands.
Additionally the '@' operator is used to simplify the line segment commands.

``(l4 @ 1).Y`` is used to extract the y-component of the ``l4 @ 1`` vector.

.. image:: assets/general_ex15.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 15]
        :end-before: [Ex. 15]

* **Algebra mode**

    Combine lines via the pattern ``Curve() + [l1, l2, l3, l4, l5]``

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 15]
        :end-before: [Ex. 15]

.. _ex 16:

16. Mirroring 3D Objects
---------------------------------------------------

Mirror can also be used with BuildPart (and BuildSketch) to mirror 3D objects.
The ``Plane.offset()`` method shifts the plane in the normal direction (positive or negative).

.. image:: assets/general_ex16.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 16]
        :end-before: [Ex. 16]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 16]
        :end-before: [Ex. 16]


.. _ex 17:

17. Mirroring From Faces
---------------------------------------------------

Here we select the farthest face in the Y-direction and turn it into a :class:`~geometry.Plane` using the
``Plane()`` class.

.. image:: assets/general_ex17.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 17]
        :end-before: [Ex. 17]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 17]
        :end-before: [Ex. 17]


.. _ex 18:

18. Creating Workplanes on Faces
---------------------------------------------------

Here we start with an earlier example, select the top face, draw a rectangle and then use Extrude
with a negative distance.

.. image:: assets/general_ex18.svg
    :align: center

* **Builder mode**

    We then use ``Mode.SUBTRACT`` to cut it out from the main body.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 18]
        :end-before: [Ex. 18]

* **Algebra mode**

    We then use ``-=`` to cut it out from the main body.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 18]
        :end-before: [Ex. 18]


.. _ex 19:

19. Locating a workplane on a vertex
---------------------------------------------------

Here a face is selected and two different strategies are used to select vertices.
Firstly ``vtx`` uses :meth:`~topology.ShapeList.group_by` and ``Axis.X`` to select a particular vertex. The second strategy uses a custom
defined Axis ``vtx2Axis`` that is pointing roughly in the direction of a vertex to select, and then :meth:`~topology.ShapeList.sort_by`
this custom Axis.

.. image:: assets/general_ex19.svg
    :align: center

* **Builder mode**

    Then the X and Y positions of these vertices are selected and passed to :class:`~build_common.Locations`
    as center points for two circles that cut through the main part. Note that if you passed the variable ``vtx`` directly to
    :class:`~build_common.Locations` then the part would be offset from the workplane by the vertex z-position.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 19]
        :end-before: [Ex. 19]

* **Algebra mode**

    Then the X and Y positions of these vertices are selected and used to move two circles
    that cut through the main part. Note that if you passed the variable ``vtx`` directly to
    :class:`~geometry.Pos` then the part would be offset from the workplane by the vertex z-position.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 19]
        :end-before: [Ex. 19]


.. _ex 20:

20. Offset Sketch Workplane
---------------------------------------------------

The ``plane`` variable is set to be coincident with the farthest face in the
negative x-direction. The resulting Plane is offset from the original position.

.. image:: assets/general_ex20.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 20]
        :end-before: [Ex. 20]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 20]
        :end-before: [Ex. 20]


.. _ex 21:

21. Create a Workplanes in the center of another shape
-------------------------------------------------------

One cylinder is created, and then the origin and z_dir of that part are used to create a new Plane for
positioning another cylinder perpendicular and halfway along the first.

.. image:: assets/general_ex21.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 21]
        :end-before: [Ex. 21]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 21]
        :end-before: [Ex. 21]


.. _ex 22:

22. Rotated Workplanes
---------------------------------------------------

It is also possible to create a rotated workplane, building upon some of the concepts in an earlier
example.

.. image:: assets/general_ex22.svg
    :align: center

* **Builder mode**

    Use the :meth:`~geometry.Plane.rotated` method to rotate the workplane.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 22]
        :end-before: [Ex. 22]

* **Algebra mode**

    Use the operator ``*`` to relocate the plane (post-multiplication!).

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 22]
        :end-before: [Ex. 22]

:class:`~build_common.GridLocations` places 4 Circles on 4 points on this rotated workplane, and then the Circles are
extruded in the "both" (positive and negative) normal direction.


.. _ex 23:

23. Revolve
---------------------------------------------------

Here we build a sketch with a :class:`~objects_curve.Polyline`,
:class:`~objects_curve.Line`, and a :class:`~objects_sketch.Circle`. It is
absolutely critical that the sketch is only on one side of the axis of rotation
before Revolve is called. To that end, ``split`` is used with ``Plane.ZY`` to keep
only one side of the Sketch.

It is highly recommended to view your sketch before you attempt to call revolve.

.. image:: assets/general_ex23.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 23]
        :end-before: [Ex. 23]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 23]
        :end-before: [Ex. 23]


.. _ex 24:

24. Loft
---------------------------------------------------

Loft is a very powerful tool that can be used to join dissimilar shapes. In this case we make a
conical-like shape from a circle and a rectangle that is offset vertically. In this case
:meth:`~operations_part.loft` automatically takes the pending faces that were added by the two BuildSketches.
Loft can behave unexpectedly when the input faces are not parallel to each other.

.. image:: assets/general_ex24.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 24]
        :end-before: [Ex. 24]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 24]
        :end-before: [Ex. 24]


.. _ex 25:

25. Offset Sketch
---------------------------------------------------

.. image:: assets/general_ex25.svg
    :align: center

* **Builder mode**

    BuildSketch faces can be transformed with a 2D :meth:`~operations_generic.offset`.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 25]
        :end-before: [Ex. 25]

* **Algebra mode**

    Sketch faces can be transformed with a 2D :meth:`~operations_generic.offset`.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 25]
        :end-before: [Ex. 25]

They can be offset inwards or outwards, and with different techniques for extending the
corners (see :class:`~build_enums.Kind` in the Offset docs).


.. _ex 26:

26. Offset Part To Create Thin features
---------------------------------------------------

Parts can also be transformed using an offset, but in this case with
a 3D :meth:`~operations_generic.offset`. Also commonly known as a shell, this allows creating thin walls
using very few operations. This can also be offset inwards or outwards. Faces can be selected to be
"deleted" using the ``openings`` parameter of :meth:`~operations_generic.offset`.

Note that self intersecting edges and/or faces can break both 2D and 3D offsets.

.. image:: assets/general_ex26.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 26]
        :end-before: [Ex. 26]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 26]
        :end-before: [Ex. 26]


.. _ex 27:

27. Splitting an Object
---------------------------------------------------

You can split an object using a plane, and retain either or both halves. In this case we select
a face and offset half the width of the box.

.. image:: assets/general_ex27.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 27]
        :end-before: [Ex. 27]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 27]
        :end-before: [Ex. 27]


.. _ex 28:

28. Locating features based on Faces
---------------------------------------------------

.. image:: assets/general_ex28.svg
    :align: center

* **Builder mode**

    We create a triangular prism with :class:`~build_enums.Mode` ``.PRIVATE`` and then later
    use the faces of this object to cut holes in a sphere.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 28]
        :end-before: [Ex. 28]

* **Algebra mode**

    We create a triangular prism and then later  use the faces of this object to cut holes in a sphere.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 28]
        :end-before: [Ex. 28]

We are able to create multiple workplanes by looping over the list of faces.


.. _ex 29:

29. The Classic OCC Bottle
---------------------------------------------------

build123d is based on the OpenCascade.org (OCC) modeling Kernel. Those who are familiar with OCC
know about the famous ‘bottle’ example. We use a 3D Offset and the openings parameter to create
the bottle opening.

.. image:: assets/general_ex29.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 29]
        :end-before: [Ex. 29]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 29]
        :end-before: [Ex. 29]


.. _ex 30:

30. Bezier Curve
---------------------------------------------------

Here ``pts`` is used as an input to both :class:`~objects_curve.Polyline` and
:class:`~objects_curve.Bezier` and ``wts`` to Bezier alone. These two together
create a closed line that is made into a face and extruded.

.. image:: assets/general_ex30.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 30]
        :end-before: [Ex. 30]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 30]
        :end-before: [Ex. 30]


.. _ex 31:

31. Nesting Locations
---------------------------------------------------

Locations contexts can be nested to create groups of shapes. Here 24 triangles, 6 squares, and
1 hexagon are created and then extruded. Notably :class:`~build_common.PolarLocations`
rotates any "children" groups by default.

.. image:: assets/general_ex31.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 31]
        :end-before: [Ex. 31]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 31]
        :end-before: [Ex. 31]


.. _ex 32:

32. Python For-Loop
---------------------------------------------------

In this example, a standard python for-loop is used along with a list of faces extracted from a sketch
to progressively modify the extrusion amount. There are 7 faces in the sketch, so this results in 7
separate calls to :meth:`~operations_part.extrude`.

.. image:: assets/general_ex32.svg
    :align: center

* **Builder mode**

    :class:`~build_enums.Mode` ``.PRIVATE`` is used in :class:`~build_sketch.BuildSketch` to avoid
    adding these faces until the for-loop.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 32]
        :end-before: [Ex. 32]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 32]
        :end-before: [Ex. 32]


.. _ex 33:

33. Python Function and For-Loop
---------------------------------------------------

Building on the previous example, a standard python function is used to return
a sketch as a function of several inputs to
progressively modify the size of each square.

.. image:: assets/general_ex33.svg
    :align: center

* **Builder mode**

    The function returns a :class:`~build_sketch.BuildSketch`.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 33]
        :end-before: [Ex. 33]

* **Algebra mode**

    The function returns a ``Sketch`` object.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 33]
        :end-before: [Ex. 33]


.. _ex 34:

34. Embossed and Debossed Text
---------------------------------------------------

.. image:: assets/general_ex34.svg
    :align: center

* **Builder mode**

    The text "Hello" is placed on top of a rectangle and embossed (raised) by placing a BuildSketch on the
    top face (``topf``). Note that :class:`~build_enums.Align` is used to control the text placement. We re-use
    the ``topf`` variable to select the same face and deboss (indented) the text "World". Note that if we simply
    ran ``BuildSketch(ex34.faces().sort_by(Axis.Z)[-1])`` for both ``ex34_sk1 & 2`` it would incorrectly locate
    the 2nd "World" text on the top of the "Hello" text.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 34]
        :end-before: [Ex. 34]

* **Algebra mode**

    The text "Hello" is placed on top of a rectangle and embossed (raised) by placing a sketch on the
    top face (``topf``). Note that :class:`~build_enums.Align` is used to control the text placement. We re-use
    the ``topf`` variable to select the same face and deboss (indented) the text "World".

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 34]
        :end-before: [Ex. 34]


.. _ex 35:

35. Slots
---------------------------------------------------

.. image:: assets/general_ex35.svg
    :align: center

* **Builder mode**

    Here we create a :class:`~objects_sketch.SlotCenterToCenter` and then use a
    :class:`~build_line.BuildLine` and :class:`~objects_curve.RadiusArc` to create an
    arc for two instances of :class:`~objects_sketch.SlotArc`.

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 35]
        :end-before: [Ex. 35]

* **Algebra mode**

    Here we create a :class:`~objects_sketch.SlotCenterToCenter` and then use
    a :class:`~objects_curve.RadiusArc` to create an arc for two instances of :class:`~operations_sketch.SlotArc`.

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 35]
        :end-before: [Ex. 35]


.. _ex 36:

36. Extrude Until
---------------------------------------------------

Sometimes you will want to extrude until a given face that could be non planar or
where you might not know easily the distance you have to extrude to. In such
cases you can use :meth:`~operations_part.extrude` :class:`~build_enums.Until`
with ``Until.NEXT`` or ``Until.LAST``.

.. image:: assets/general_ex36.svg
    :align: center

* **Builder mode**

    .. literalinclude:: general_examples.py
        :start-after: [Ex. 36]
        :end-before: [Ex. 36]

* **Algebra mode**

    .. literalinclude:: general_examples_algebra.py
        :start-after: [Ex. 36]
        :end-before: [Ex. 36]



================================================
FILE: docs/joints.rst
================================================
.. _joints:

######
Joints
######

:class:`~topology.Joint`'s enable Solid and Compound objects to be arranged
relative to each other in an intuitive manner - with the same degree of motion
that is found with the equivalent physical joints.  :class:`~topology.Joint`'s always work
in pairs - a :class:`~topology.Joint` can only be connected to another :class:`~topology.Joint` as follows:

+---------------------------------------+---------------------------------------------------------------------+--------------------+
| :class:`~topology.Joint`              | connect_to                                                          | Example            |
+=======================================+=====================================================================+====================+
| :class:`~joints.BallJoint`            |  :class:`~joints.RigidJoint`                                        | Gimbal             |
+---------------------------------------+---------------------------------------------------------------------+--------------------+
| :class:`~joints.CylindricalJoint`     |  :class:`~joints.RigidJoint`                                        | Screw              |
+---------------------------------------+---------------------------------------------------------------------+--------------------+
| :class:`~joints.LinearJoint`          | :class:`~joints.RigidJoint`, :class:`~joints.RevoluteJoint`         | Slider or Pin Slot |
+---------------------------------------+---------------------------------------------------------------------+--------------------+
| :class:`~joints.RevoluteJoint`        | :class:`~joints.RigidJoint`                                         | Hinge              |
+---------------------------------------+---------------------------------------------------------------------+--------------------+
| :class:`~joints.RigidJoint`           | :class:`~joints.RigidJoint`                                         | Fixed              |
+---------------------------------------+---------------------------------------------------------------------+--------------------+

Objects may have many joints bound to them each with an identifying label. All :class:`~topology.Joint`
objects have a ``symbol`` property that can be displayed to help visualize
their position and orientation (the `ocp-vscode <https://github.com/bernhard-42/vscode-ocp-cad-viewer>`_ viewer
has built-in support for displaying joints).

.. note::
    If joints are created within the scope of a :class:`~build_part.BuildPart` builder, the ``to_part``
    parameter need not be specified as the builder will, on exit, automatically transfer the joints created in its
    scope to the part created.

The following sections provide more detail on the available joints and describes how they are used.

.. py:module:: joints

***********
Rigid Joint
***********

A rigid joint positions two components relative to each another with no freedom of movement. When a
:class:`~joints.RigidJoint` is instantiated it's assigned a ``label``, a part to bind to (``to_part``),
and a ``joint_location`` which defines both the position and orientation of the joint (see
:class:`~geometry.Location`) - as follows:

.. code-block:: python

    RigidJoint(label="outlet", to_part=pipe, joint_location=path.location_at(1))

Once a joint is bound to a part this way, the :meth:`~topology.Joint.connect_to` method can be used to
repositioning another part relative to ``self`` which stay fixed - as follows:

.. code-block:: python

    pipe.joints["outlet"].connect_to(flange_outlet.joints["pipe"])

.. note::
    Within a part all of the joint labels must be unique.

The :meth:`~topology.Joint.connect_to` method only does a one time re-position of a part and does not
bind them in any way; however, putting them into an :ref:`assembly` will maintain there relative locations
as will combining parts with boolean operations or within a :class:`~build_part.BuildPart` context.

As a example of creating parts with joints and connecting them together, consider the following code where
flanges are attached to the ends of a curved pipe:

.. image:: assets/rigid_joints_pipe.png

.. literalinclude:: rigid_joints_pipe.py
    :emphasize-lines: 19-20, 23-24

Note how the locations of the joints are determined by the :meth:`~topology.Mixin1D.location_at` method
and how the ``-`` negate operator is used to reverse the direction of the location without changing its
position.  Also note that the ``WeldNeckFlange`` class predefines two joints, one at the pipe end and
one at the face end - both of which are shown in the above image (generated by ocp-vscode with the
``render_joints=True`` flag set in the ``show`` function).


.. autoclass:: RigidJoint

..
    :exclude-members: connect_to

    .. method:: connect_to(other: BallJoint, *, angles: RotationLike = None)
    .. method:: connect_to(other: CylindricalJoint, *, position: float = None, angle: float = None)
        :noindex:
    .. method:: connect_to(other: LinearJoint, *, position: float = None)
        :noindex:
    .. method:: connect_to(other: RevoluteJoint, *, angle: float = None)
        :noindex:
    .. method:: connect_to(other: RigidJoint)
        :noindex:

        Connect the ``RigidJoint`` to another Joint.
..



**************
Revolute Joint
**************

Component rotates around axis like a hinge. The :ref:`joint_tutorial` covers Revolute Joints in detail.

During instantiation of a :class:`~joints.RevoluteJoint` there are three parameters not present with
Rigid Joints: ``axis``, ``angle_reference``, and ``range`` that allow the circular motion to be fully
defined.

When :meth:`~topology.Joint.connect_to` with a Revolute Joint, an extra ``angle`` parameter is present
which allows one to change the relative position of joined parts by changing a single value.

.. autoclass:: RevoluteJoint

..
    :exclude-members: connect_to

    .. method:: connect_to(other: RigidJoint, *, angle: float = None)

        Connect the ``RevoluteJoint`` to a ``RigidJoint``

************
Linear Joint
************

Component moves along a single axis as with a sliding latch shown here:

.. image:: assets/joint-latch-slide.png

The code to generate these components follows:

.. literalinclude:: slide_latch.py
    :emphasize-lines: 30, 52, 55

.. image:: assets/joint-latch.png
    :width: 65 %
.. image:: assets/joint-slide.png
    :width: 27.5 %

Note how the slide is constructed in a different orientation than the direction of motion. The
three highlighted lines of code show how the joints are created and connected together:

* The :class:`~joints.LinearJoint` has an axis and limits of movement
* The :class:`~joints.RigidJoint` has a single location, orientated such that the knob will ultimately be "up"
* The ``connect_to`` specifies a position that must be within the predefined limits.

The slider can be moved back and forth by just changing the ``position`` value.  Values outside
of the limits will raise an exception.

.. autoclass:: LinearJoint

..
    :exclude-members: connect_to

    .. method:: connect_to(other: RevoluteJoint, *, position: float = None, angle: float = None)
    .. method:: connect_to(other: RigidJoint, *, position: float = None)
        :noindex:

        Connect the ``LinearJoint`` to either a ``RevoluteJoint`` or ``RigidJoint``

*****************
Cylindrical Joint
*****************

A :class:`~joints.CylindricalJoint` allows a component to rotate around and moves along a single axis
like a screw combining the functionality of a :class:`~joints.LinearJoint` and a
:class:`~joints.RevoluteJoint` joint.  The ``connect_to`` for these joints have both ``position`` and
``angle`` parameters as shown below extracted from the joint tutorial.


.. code-block::python

    hinge_outer.joints["hole2"].connect_to(m6_joint, position=5 * MM, angle=30)

.. autoclass:: CylindricalJoint

..
    :exclude-members: connect_to

    .. method:: connect_to(other: RigidJoint, *, position: float = None, angle: float = None)

        Connect the ``CylindricalJoint`` to a ``RigidJoint``

**********
Ball Joint
**********

A component rotates around all 3 axes using a gimbal system (3 nested rotations). A :class:`~joints.BallJoint`
is found within a rod end as shown here:

.. image:: assets/rod_end.png

.. literalinclude:: rod_end.py
    :emphasize-lines: 40-44,51,53

Note how limits are defined during the instantiation of the ball joint when ensures that the pin or bolt
within the rod end does not interfere with the rod end itself. The ``connect_to`` sets the three angles
(only two are significant in this example).

.. autoclass:: BallJoint

..
    :exclude-members: connect_to

    .. method:: connect_to(other: RigidJoint, *, angles: RotationLike = None)

        Connect a ``BallJoint`` to a ``RigidJoint``



================================================
FILE: docs/key_concepts.rst
================================================
############
Key Concepts
############

The following key concepts will help new users understand build123d quickly.

.. _topology:

Topology
========

Topology, in the context of 3D modeling and computational geometry, is the
branch of mathematics that deals with the properties and relationships of
geometric objects that are preserved under continuous deformations. In the
context of CAD and modeling software like build123d, topology refers to the
hierarchical structure of geometric elements (vertices, edges, faces, etc.) and
their relationships in a 3D model. This structure defines how the components of
a model are connected, enabling operations like Boolean operations,
transformations, and analysis of complex shapes. Topology provides a formal
framework for understanding and manipulating geometric data in a consistent and
reliable manner.

The following are the topological objects that compose build123d objects:

:class:`~topology.Vertex`
    A Vertex is a data structure representing a 0D topological element. It
    defines a precise point in 3D space, often at the endpoints or intersections of
    edges in a 3D model. These vertices are part of the topological structure used
    to represent complex shapes in build123d.

:class:`~topology.Edge`
	An Edge in build123d is a fundamental geometric entity representing a 1D
	element in a 3D model. It defines the shape and position of a 1D curve within
	the model. Edges play a crucial role in defining the boundaries of faces and in
	constructing complex 3D shapes.

:class:`~topology.Wire`
	A Wire in build123d is a topological construct that represents a connected
	sequence of Edges, forming a 1D closed or open loop within a 3D model. Wires
	define the boundaries of faces and can be used to create complex shapes, making
	them essential for modeling in build123d.

:class:`~topology.Face`
	A Face in build123d represents a 2D surface in a 3D model. It defines the
	boundary of a region and can have associated geometric and topological data.
	Faces are vital for shaping solids, providing surfaces where other elements like
	edges and wires are connected to form complex structures.

:class:`~topology.Shell`
	A Shell in build123d represents a collection of Faces, defining a closed,
	connected volume in 3D space. It acts as a container for organizing and grouping
	faces into a single shell, essential for defining complex 3D shapes like solids
	or assemblies within the build123d modeling framework.

:class:`~topology.Solid`
	A Solid in build123d is a 3D geometric entity that represents a bounded
	volume with well-defined interior and exterior surfaces. It encapsulates a
	closed and watertight shape, making it suitable for modeling solid objects and
	enabling various Boolean operations such as union, intersection, and
	subtraction.

:class:`~topology.Compound`
	A Compound in build123d is a container for grouping multiple geometric
	shapes. It can hold various types of entities, such as vertices, edges, wires,
	faces, shells, or solids, into a single structure. This makes it a versatile
	tool for managing and organizing complex assemblies or collections of shapes
	within a single container.

:class:`~topology.Shape`
	A Shape in build123d represents a fundamental building block in 3D
	modeling. It encompasses various topological elements like vertices, edges,
	wires, faces, shells, solids, and compounds. The Shape class is the base class
	for all of the above topological classes.

One can use the :meth:`~topology.Shape.show_topology` method to display the
topology of a shape as shown here for a unit cube:

.. code::
	
	Solid                      at 0x7f94c55430f0, Center(0.5, 0.5, 0.5)
	└── Shell                  at 0x7f94b95835f0, Center(0.5, 0.5, 0.5)
	    ├── Face               at 0x7f94b95836b0, Center(0.0, 0.5, 0.5)
	    │   └── Wire           at 0x7f94b9583730, Center(0.0, 0.5, 0.5)
	    │       ├── Edge       at 0x7f94b95838b0, Center(0.0, 0.0, 0.5)
	    │       │   ├── Vertex at 0x7f94b9583470, Center(0.0, 0.0, 1.0)
	    │       │   └── Vertex at 0x7f94b9583bb0, Center(0.0, 0.0, 0.0)
	    │       ├── Edge       at 0x7f94b9583a30, Center(0.0, 0.5, 1.0)
	    │       │   ├── Vertex at 0x7f94b9583030, Center(0.0, 1.0, 1.0)
	    │       │   └── Vertex at 0x7f94b9583e70, Center(0.0, 0.0, 1.0)
	    │       ├── Edge       at 0x7f94b9583770, Center(0.0, 1.0, 0.5)
	    │       │   ├── Vertex at 0x7f94b9583bb0, Center(0.0, 1.0, 1.0)
	    │       │   └── Vertex at 0x7f94b9583e70, Center(0.0, 1.0, 0.0)
	    │       └── Edge       at 0x7f94b9583db0, Center(0.0, 0.5, 0.0)
	    │           ├── Vertex at 0x7f94b9583e70, Center(0.0, 1.0, 0.0)
	    │           └── Vertex at 0x7f94b95862f0, Center(0.0, 0.0, 0.0)
	...
	    └── Face               at 0x7f94b958d3b0, Center(0.5, 0.5, 1.0)
	        └── Wire           at 0x7f94b958d670, Center(0.5, 0.5, 1.0)
	            ├── Edge       at 0x7f94b958e130, Center(0.0, 0.5, 1.0)
	            │   ├── Vertex at 0x7f94b958e330, Center(0.0, 1.0, 1.0)
	            │   └── Vertex at 0x7f94b958e770, Center(0.0, 0.0, 1.0)
	            ├── Edge       at 0x7f94b958e630, Center(0.5, 1.0, 1.0)
	            │   ├── Vertex at 0x7f94b958e8b0, Center(1.0, 1.0, 1.0)
	            │   └── Vertex at 0x7f94b958ea70, Center(0.0, 1.0, 1.0)
	            ├── Edge       at 0x7f94b958e7b0, Center(1.0, 0.5, 1.0)
	            │   ├── Vertex at 0x7f94b958ebb0, Center(1.0, 1.0, 1.0)
	            │   └── Vertex at 0x7f94b958ed70, Center(1.0, 0.0, 1.0)
	            └── Edge       at 0x7f94b958eab0, Center(0.5, 0.0, 1.0)
	                ├── Vertex at 0x7f94b958eeb0, Center(1.0, 0.0, 1.0)
	                └── Vertex at 0x7f94b9592170, Center(0.0, 0.0, 1.0)
	
Users of build123d will often reference topological objects as part of the
process of creating the object as described below.

Location
========

A :class:`~geometry.Location` represents a combination of translation and rotation
applied to a topological or geometric object. It encapsulates information
about the spatial orientation and position of a shape within its reference
coordinate system. This allows for efficient manipulation of shapes within
complex assemblies or transformations. The location is typically used to
position shapes accurately within a 3D scene, enabling operations like
assembly, and boolean operations. It's an essential component in build123d
for managing the spatial relationships of geometric entities, providing a
foundation for precise 3D modeling and engineering applications.

The topological classes (sub-classes of :class:`~topology.Shape`) and the geometric classes 
:class:`~geometry.Axis` and :class:`~geometry.Plane` all have a ``location`` property.
The :class:`~geometry.Location` class itself has ``position`` and ``orientation`` properties
that have setters and getters as shown below:


.. doctest::

    >>> from build123d import *
    >>> # Create an object and extract its location
    >>> b = Box(1, 1, 1)
    >>> box_location = b.location
    >>> box_location
    (p=(0.00, 0.00, 0.00), o=(-0.00, 0.00, -0.00))
    >>> # Set position and orientation independently
    >>> box_location.position = (1, 2, 3)
    >>> box_location.orientation = (30, 40, 50)
    >>> box_location.position
    Vector: (1.0, 2.0, 3.0)
    >>> box_location.orientation
    Vector: (29.999999999999993, 40.00000000000002, 50.000000000000036)

Combining the getter and setter enables relative changes as follows:

.. doctest::

    >>> # Relative change
    >>> box_location.position += (3, 2, 1)
    >>> box_location.position
    Vector: (4.0, 4.0, 4.0)

There are also four methods that are used to change the location of objects:

* :meth:`~topology.Shape.locate` - absolute change of this object
* :meth:`~topology.Shape.located` - absolute change of copy of this object
* :meth:`~topology.Shape.move` - relative change of this object
* :meth:`~topology.Shape.moved` - relative change of copy of this object

Locations can be combined with the ``*`` operator and have their direction flipped with
the ``-`` operator.

Selectors
=========

.. include:: selectors.rst



================================================
FILE: docs/key_concepts_algebra.rst
================================================
###########################
Key Concepts (algebra mode)
###########################

Build123d's algebra mode works on objects of the classes ``Shape``, ``Part``, ``Sketch`` and ``Curve`` and is based on two concepts:

1. **Object arithmetic**
2. **Placement arithmetic**

Object arithmetic
=====================

-   Creating a box and a cylinder centered at ``(0, 0, 0)``

    .. code-block:: python

        b = Box(1, 2, 3)
        c = Cylinder(0.2, 5)

-   Fusing a box and a cylinder

    .. code-block:: python

        r = Box(1, 2, 3) + Cylinder(0.2, 5)

-   Cutting a cylinder from a box

    .. code-block:: python

        r = Box(1, 2, 3) - Cylinder(0.2, 5)

-   Intersecting a box and a cylinder

    .. code-block:: python

        r = Box(1, 2, 3) & Cylinder(0.2, 5)

**Notes:**

* `b`, `c` and `r` are instances of class ``Compound`` and can be viewed with every viewer that can show ``build123d.Compound`` objects.
* A discussion around performance can be found in :ref:`algebra_performance`.
* A mathematically formal definition of the algebra can be found in :ref:`algebra_definition`.


Placement arithmetic
=======================

A ``Part``, ``Sketch`` or ``Curve`` does not have any location or rotation parameter.
The rationale is that an object defines its topology (shape, sizes and its center), but does not know 
where in space it will be located. Instead, it will be relocated with the ``*`` operator onto a plane 
and to location relative to the plane (similar ``moved``). 

The generic forms of object placement are:

1. Placement on ``plane`` or at ``location`` relative to XY plane:

    .. code-block:: python

        plane * alg_compound
        location * alg_compound

2. Placement on the ``plane`` and then moved relative to the ``plane`` by ``location`` 
(the location is relative to the local coordinate system of the plane).

    .. code-block:: python

        plane * location * alg_compound


Details can be found in :ref:`location_arithmetics`.

Examples:

-   Box on the ``XY`` plane, centered at `(0, 0, 0)` (both forms are equivalent):

    .. code-block:: python

        Plane.XY * Box(1, 2, 3)

        Box(1, 2, 3)

    Note: On the ``XY`` plane no placement is needed (mathematically ``Plane.XY *`` will not change the 
    location of an object).

-   Box on the ``XY`` plane centered at `(0, 1, 0)` (all three are equivalent):

    .. code-block:: python

        Plane.XY * Pos(0, 1, 0) * Box(1, 2, 3)

        Pos(0, 1, 0) * Box(1, 2, 3) 

        Pos(Y=1) * Box(1, 2, 3)

    Note: Again, ``Plane.XY`` can be omitted.

-   Box on plane ``Plane.XZ``:

    .. code-block:: python

        Plane.XZ * Box(1, 2, 3)

-   Box on plane ``Plane.XZ`` with a location ``(X=1, Y=2, Z=3)`` relative to the ``XZ`` plane, i.e., 
    using the x-, y- and z-axis of the ``XZ`` plane:

    .. code-block:: python

        Plane.XZ * Pos(1, 2, 3) * Box(1, 2, 3)

-   Box on plane ``Plane.XZ`` moved to ``(X=1, Y=2, Z=3)`` relative to this plane and rotated there 
    by the angles `(X=0, Y=100, Z=45)` around ``Plane.XZ`` axes:

    .. code-block:: python

        Plane.XZ * Pos(1, 2, 3) * Rot(0, 100, 45) * Box(1, 2, 3)

        Location((1, 2, 3), (0, 100, 45)) * Box(1, 2, 3)

    Note: ``Pos * Rot`` is the same as using ``Location`` directly

-   Box on plane ``Plane.XZ`` rotated on this plane by the angles ``(X=0, Y=100, Z=45)`` (using the 
    x-, y- and z-axis of the ``XZ`` plane) and then moved to ``(X=1, Y=2, Z=3)`` relative to the ``XZ`` plane:

    .. code-block:: python

        Plane.XZ * Rot(0, 100, 45) * Pos(0,1,2) * Box(1, 2, 3)


Combing both concepts
==========================

**Object arithmetic** and **Placement at locations** can be combined:

 .. code-block:: python

    b = Plane.XZ * Rot(X=30) * Box(1, 2, 3) + Plane.YZ * Pos(X=-1) * Cylinder(0.2, 5)

**Note:** In Python ``*`` binds stronger then ``+``, ``-``, ``&``, hence brackets are not needed.




================================================
FILE: docs/key_concepts_builder.rst
================================================
###########################
Key Concepts (builder mode)
###########################

There are two primary APIs provided by build123d: builder and algebra. The builder
API may be easier for new users as it provides some assistance and shortcuts; however,
if you know what a Quaternion is you might prefer the algebra API which allows
CAD objects to be created in the style of mathematical equations. Both API can
be mixed in the same model with the exception that the algebra API can't be used
from within a builder context. As with music, there is no "best" genre or API,
use the one you prefer or both if you like.

The following key concepts will help new users understand build123d quickly.

Understanding the Builder Paradigm
==================================

The **Builder** paradigm in build123d provides a powerful and intuitive way to construct 
complex geometric models. At its core, the Builder works like adding a column of numbers 
on a piece of paper: a running "total" is maintained internally as each new object is 
added or modified. This approach simplifies the process of constructing models by breaking 
it into smaller, incremental steps.

How the Builder Works
----------------------

When using a Builder (such as **BuildLine**, **BuildSketch**, or **BuildPart**), the 
following principles apply:

1. **Running Total**:
   - The Builder maintains an internal "total," which represents the current state of 
   the object being built. 
   - Each operation updates this total by combining the new object with the existing one.

2. **Combination Modes**:
   - Just as numbers in a column may have a `+` or `-` sign to indicate addition or 
   subtraction, Builders use **modes** to control how each object is combined with 
   the current total.
   - Common modes include:

     - **ADD**: Adds the new object to the current total.
     - **SUBTRACT**: Removes the new object from the current total.
     - **INTERSECT**: Keeps only the overlapping regions of the new object and the current total.
     - **REPLACE**: Entirely replace the running total.
     - **PRIVATE**: Don't change the running total at all. 

   - The mode can be set dynamically for each operation, allowing for flexible and precise modeling.

3. **Extracting the Result**:
   - At the end of the building process, the final object is accessed through the 
   Builder's attributes, such as ``.line``, ``.sketch``, or ``.part``, depending on 
   the Builder type.
   - For example:
   
     - **BuildLine**: Use ``.line`` to retrieve the final wireframe geometry.
     - **BuildSketch**: Use ``.sketch`` to extract the completed 2D profile.
     - **BuildPart**: Use ``.part`` to obtain the 3D solid.

Example Workflow
-----------------

Here is an example of using a Builder to create a simple part:

.. code-block:: python

    from build123d import *

    # Using BuildPart to create a 3D model
    with BuildPart() as example_part:
        with BuildSketch() as base_sketch:
            Rectangle(20, 20)
        extrude(amount=10)  # Create a base block
        with BuildSketch(Plane(example_part.faces().sort_by(Axis.Z).last)) as cut_sketch:
            Circle(5)
        extrude(amount=-5, mode=Mode.SUBTRACT)  # Subtract a cylinder

    # Access the final part
    result_part = example_part.part

Key Concepts
------------

- **Incremental Construction**:
  Builders allow you to build objects step-by-step, maintaining clarity and modularity.
  
- **Dynamic Mode Switching**:
  The **mode** parameter gives you precise control over how each operation modifies 
  the current total.

- **Seamless Extraction**:
  The Builder paradigm simplifies the retrieval of the final object, ensuring that you 
  always have access to the most up-to-date result.

Analogy: Adding Numbers on Paper
--------------------------------

Think of the Builder as a running tally when adding numbers on a piece of paper:

- Each number represents an operation or object.
- The ``+`` or ``-`` sign corresponds to the **ADD** or **SUBTRACT** mode.
- At the end, the total is the sum of all operations, which you can retrieve by referencing 
  the Builder’s output.

By adopting this approach, build123d ensures a natural, intuitive workflow for constructing 
2D and 3D models.

Builders
========

The three builders, ``BuildLine``, ``BuildSketch``, and ``BuildPart`` are tools to create
new objects - not the objects themselves. Each of the objects and operations applicable
to these builders create objects of the standard CadQuery Direct API, most commonly
``Compound`` objects.  This is opposed to CadQuery's Fluent API which creates objects
of the ``Workplane`` class which frequently needed to be converted back to base
class for further processing.

One can access the objects created by these builders by referencing the appropriate
instance variable. For example:

.. code-block:: python

    with BuildPart() as my_part:
        ...

    show_object(my_part.part)

.. code-block:: python

    with BuildSketch() as my_sketch:
        ...

    show_object(my_sketch.sketch)

.. code-block:: python

    with BuildLine() as my_line:
        ...

    show_object(my_line.line)

Implicit Builder Instance Variables
===================================

One might expect to have to reference a builder's instance variable when using
objects or operations that impact that builder like this:

.. code-block:: python

    with BuildPart() as part_builder:
        Box(part_builder, 10,10,10)

Instead, build123d determines from the scope of the object or operation which
builder it applies to thus eliminating the need for the user to provide this
information - as follows:

.. code-block:: python

    with BuildPart() as part_builder:
        Box(10,10,10)
        with BuildSketch() as sketch_builder:
            Circle(2)

In this example, ``Box`` is in the scope of ``part_builder`` while ``Circle``
is in the scope of ``sketch_builder``.

Workplanes
==========

As build123d is a 3D CAD package one must be able to position objects anywhere. As one
frequently will work in the same plane for a sequence of operations, the first parameter(s)
of the builders is a (sequence of) workplane(s) which is (are) used
to aid in the location of features. The default workplane in most cases is the ``Plane.XY``
where a tuple of numbers represent positions on the x and y axes. However workplanes can
be generated on any plane which allows users to put a workplane where they are working
and then work in local 2D coordinate space.


.. code-block:: python

    with BuildPart(Plane.XY) as example:
        ... # a 3D-part
        with BuildSketch(example.faces().sort_by(sort_by=Axis.Z)[0]) as bottom:
            ...
        with BuildSketch(Plane.XZ) as vertical:
            ...
        with BuildSketch(example.faces().sort_by(sort_by=Axis.Z)[-1]) as top:
            ...

When ``BuildPart`` is invoked it creates the workplane provided as a parameter (which has a
default of the ``Plane.XY``). The ``bottom`` sketch is therefore created on the ``Plane.XY`` but with the
normal reversed to point down. Subsequently the user has created the ``vertical`` (``Plane.XZ``) sketch.
All objects or operations within the scope of a workplane will automatically be orientated with
respect to this plane so the user only has to work with local coordinates.

As shown above, workplanes can be created from faces as well. The ``top`` sketch is
positioned on top of ``example`` by selecting its faces and finding the one with the greatest z value.

One is not limited to a single workplane at a time. In the following example all six
faces of the first box are used to define workplanes which are then used to position
rotated boxes.

.. code-block:: python

    import build123d as bd

    with bd.BuildPart() as bp:
        bd.Box(3, 3, 3)
        with bd.BuildSketch(*bp.faces()):
            bd.Rectangle(1, 2, rotation=45)
        bd.extrude(amount=0.1)

This is the result:

.. image:: boxes_on_faces.svg
  :align: center

.. _location_context_link:

Locations Context
=================

When positioning objects or operations within a builder Location Contexts are used.  These
function in a very similar was to the builders in that they create a context where one or
more locations are active within a scope.  For example:

.. code-block:: python

    with BuildPart():
        with Locations((0,10),(0,-10)):
            Box(1,1,1)
            with GridLocations(x_spacing=5, y_spacing=5, x_count=2, y_count=2):
                Sphere(1)
            Cylinder(1,1)

In this example ``Locations`` creates two positions on the current workplane at (0,10) and (0,-10).
Since ``Box`` is within the scope of ``Locations``, two boxes are created at these locations. The
``GridLocations`` context creates four positions which apply to the ``Sphere``. The ``Cylinder`` is
out of the scope of ``GridLocations`` but in the scope of ``Locations`` so two cylinders are created.

Note that these contexts are creating Location objects not just simple points. The difference
isn't obvious until the ``PolarLocations`` context is used which can also rotate objects within
its scope - much as the hour and minute indicator on an analogue clock.

Also note that the locations are local to the current location(s) - i.e. ``Locations`` can be
nested. It's easy for a user to retrieve the global locations:

.. code-block:: python

    with Locations(Plane.XY, Plane.XZ):
        locs = GridLocations(1, 1, 2, 2)
        for l in locs:
            print(l)

.. code-block::

    Location(p=(-0.50,-0.50,0.00), o=(0.00,-0.00,0.00))
    Location(p=(-0.50,0.50,0.00), o=(0.00,-0.00,0.00))
    Location(p=(0.50,-0.50,0.00), o=(0.00,-0.00,0.00))
    Location(p=(0.50,0.50,0.00), o=(0.00,-0.00,0.00))
    Location(p=(-0.50,-0.00,-0.50), o=(90.00,-0.00,0.00))
    Location(p=(-0.50,0.00,0.50), o=(90.00,-0.00,0.00))
    Location(p=(0.50,0.00,-0.50), o=(90.00,-0.00,0.00))
    Location(p=(0.50,0.00,0.50), o=(90.00,-0.00,0.00))


Operation Inputs
================

When one is operating on an existing object, e.g. adding a fillet to a part,
an iterable of objects is often required (often a ShapeList).

Here is the definition of :meth:`~operations_generic.fillet` to help illustrate:

.. code-block:: python

    def fillet(
        objects: Union[Union[Edge, Vertex], Iterable[Union[Edge, Vertex]]],
        radius: float,
    ):

To use this fillet operation, an edge or vertex or iterable of edges or 
vertices must be provided followed by a fillet radius with or without the keyword as follows:

.. code-block:: python

    with BuildPart() as pipes:
        Box(10, 10, 10, rotation=(10, 20, 30))
        ...
        fillet(pipes.edges(Select.LAST), radius=0.2)

Here the fillet accepts the iterable ShapeList of edges from the last operation of
the ``pipes`` builder and a radius is provided as a keyword argument.

Combination Modes
=================

Almost all objects or operations have a ``mode`` parameter which is defined by the
``Mode`` Enum class as follows:

.. code-block:: python

    class Mode(Enum):
        ADD = auto()
        SUBTRACT = auto()
        INTERSECT = auto()
        REPLACE = auto()
        PRIVATE = auto()

The ``mode`` parameter describes how the user would like the object or operation to
interact with the object within the builder. For example, ``Mode.ADD`` will
integrate a new object(s) in with an existing ``part``.  Note that a part doesn't
necessarily have to be a single object so multiple distinct objects could be added
resulting is multiple objects stored as a ``Compound`` object. As one might expect
``Mode.SUBTRACT``, ``Mode.INTERSECT``, and ``Mode.REPLACE`` subtract, intersect, or replace
(from) the builder's object. ``Mode.PRIVATE`` instructs the builder that this object
should not be combined with the builder's object in any way.

Most commonly, the default ``mode`` is ``Mode.ADD`` but this isn't always true.
For example, the ``Hole`` classes use a default ``Mode.SUBTRACT`` as they remove
a volume from the part under normal circumstances. However, the ``mode`` used in
the ``Hole`` classes can be specified as ``Mode.ADD`` or ``Mode.INTERSECT`` to
help in inspection or debugging.


Using Locations & Rotating Objects
==================================

build123d stores points (to be specific ``Location`` (s)) internally to be used as
positions for the placement of new objects.  By default, a single location
will be created at the origin of the given workplane such that:

.. code-block:: python

    with BuildPart() as pipes:
        Box(10, 10, 10, rotation=(10, 20, 30))

will create a single 10x10x10 box centered at (0,0,0) - by default objects are
centered. One can create multiple objects by pushing points prior to creating
objects as follows:

.. code-block:: python

    with BuildPart() as pipes:
        with Locations((-10, -10, -10), (10, 10, 10)):
            Box(10, 10, 10, rotation=(10, 20, 30))

which will create two boxes.

To orient a part, a ``rotation`` parameter is available on ``BuildSketch``` and
``BuildPart`` APIs. When working in a sketch, the rotation is a single angle in
degrees so the parameter is a float. When working on a part, the rotation is
a three dimensional ``Rotation`` object of the form
``Rotation(<about x>, <about y>, <about z>)`` although a simple three tuple of
floats can be used as input.  As 3D rotations are not cumulative, one can
combine rotations with the `*` operator like this:
``Rotation(10, 20, 30) * Rotation(0, 90, 0)`` to generate any desired rotation.

.. hint::
    Experts Only

    ``Locations`` will accept ``Location`` objects for input which allows one
    to specify both the position and orientation.  However, the orientation
    is often determined by the ``Plane`` that an object was created on.
    ``Rotation`` is a subclass of ``Location`` and therefore will also accept
    a position component.

Builder's Pending Objects
=========================

When a builder exits, it will push the object created back to its parent if
there was one.  Here is an example:

.. code-block:: python

    height, width, thickness, f_rad = 60, 80, 20, 10

    with BuildPart() as pillow_block:
        with BuildSketch() as plan:
            Rectangle(width, height)
            fillet(plan.vertices(), radius=f_rad)
        extrude(amount=thickness)

``BuildSketch`` exits after the ``fillet`` operation and when doing so it transfers
the sketch to the ``pillow_block`` instance of ``BuildPart`` as the internal instance variable
``pending_faces``. This allows the ``extrude`` operation to be immediately invoked as it
extrudes these pending faces into ``Solid`` objects. Likewise, ``loft`` would take all of the
``pending_faces`` and attempt to create a single ``Solid`` object from them.

Normally the user will not need to interact directly with pending objects; however,
one can see pending Edges and Faces with ``<builder_instance>.pending_edges`` and 
``<builder_instance>.pending_faces`` attributes.  In the above example, by adding a 
``print(pillow_block.pending_faces)`` prior to the ``extrude(amount=thickness)`` the
pending ``Face`` from the ``BuildSketch`` will be displayed.



================================================
FILE: docs/line_types.py
================================================
"""
Create line type examples

name: line_types.py
by:   Gumyr
date: July 25th 2023

desc:
    This python module generates sample of all the available line types.

license:

    Copyright 2023 Gumyr

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""

from build123d import *

exporter = ExportSVG(scale=1)
exporter.add_layer(name="Text", fill_color=(0, 0, 0))
line_types = [l for l in LineType.__members__]
text_locs = Pos((100, 0, 0)) * GridLocations(0, 6, 1, len(line_types)).locations
line_locs = Pos((105, 0, 0)) * GridLocations(0, 6, 1, len(line_types)).locations
for line_type, text_loc, line_loc in zip(line_types, text_locs, line_locs):
    exporter.add_layer(name=line_type, line_type=getattr(LineType, line_type))
    exporter.add_shape(
        Compound.make_text(
            "LineType." + line_type,
            font_size=5,
            align=(Align.MAX, Align.CENTER),
        ).locate(text_loc),
        layer="Text",
    )
    exporter.add_shape(
        Edge.make_line((0, 0), (100, 0)).locate(line_loc), layer=line_type
    )
exporter.write("assets/line_types.svg")



================================================
FILE: docs/location_arithmetic.rst
================================================
.. _location_arithmetics:

Location arithmetic for algebra mode
======================================


Position a shape relative to the XY plane
---------------------------------------------

For the following use the helper function:

.. code-block:: python

    def location_symbol(location: Location, scale: float = 1) -> Compound:
        return Compound.make_triad(axes_scale=scale).locate(location)

    def plane_symbol(plane: Plane, scale: float = 1) -> Compound:
        triad = Compound.make_triad(axes_scale=scale)
        circle = Circle(scale * .8).edge()
        return (triad + circle).locate(plane.location)


1. **Positioning at a location**

    .. code-block:: python

        loc = Location((0.1, 0.2, 0.3), (10, 20, 30))

        face = loc * Rectangle(1,2)

        show_object(face, name="face")
        show_object(location_symbol(loc), name="location")

    .. image:: assets/location-example-01.png

2) **Positioning on a plane**

    .. code-block:: python

        plane = Plane.XZ

        face = plane * Rectangle(1, 2)

        show_object(face, name="face")
        show_object(plane_symbol(plane), name="plane")

    .. image:: assets/location-example-07.png

    Note that the ``x``-axis and the ``y``-axis of the plane are on the ``x``-axis and the ``z``-axis of the world coordinate system (red and blue axis)


Relative positioning to a plane
------------------------------------

1. **Position an object on a plane relative to the plane**

    .. code-block:: python

        loc = Location((0.1, 0.2, 0.3), (10, 20, 30))

        face = loc * Rectangle(1,2)

        box = Plane(loc) * Pos(0.2, 0.4, 0.1) * Box(0.2, 0.2, 0.2)
        # box = Plane(face.location) * Pos(0.2, 0.4, 0.1) * Box(0.2, 0.2, 0.2)
        # box = loc * Pos(0.2, 0.4, 0.1) * Box(0.2, 0.2, 0.2)

        show_object(face, name="face")
        show_object(location_symbol(loc), name="location")
        show_object(box, name="box")

    .. image:: assets/location-example-02.png

    The ``x``, ``y``, ``z`` components of ``Pos(0.2, 0.4, 0.1)`` are relative to the ``x``-axis, ``y``-axis or
    ``z``-axis of the underlying location ``loc``.

    Note: ``Plane(loc) *``, ``Plane(face.location) *`` and ``loc *`` are equivalent in this example.

2. **Rotate an object on a plane relative to the plane**

    .. code-block:: python

        loc = Location((0.1, 0.2, 0.3), (10, 20, 30))

        face = loc * Rectangle(1,2)

        box = Plane(loc) * Rot(z=80) * Box(0.2, 0.2, 0.2)

        show_object(face, name="face")
        show_object(location_symbol(loc), name="location")
        show_object(box, name="box")

    .. image:: assets/location-example-03.png

    The box is rotated via ``Rot(z=80)`` around the ``z``-axis of the underlying location
    (and not of the z-axis of the world).

    More general:

    .. code-block:: python

        loc = Location((0.1, 0.2, 0.3), (10, 20, 30))

        face = loc * Rectangle(1,2)

        box = loc * Rot(20, 40, 80) * Box(0.2, 0.2, 0.2)

        show_object(face, name="face")
        show_object(location_symbol(loc), name="location")
        show_object(box, name="box")

    .. image:: assets/location-example-04.png

    The box is rotated via ``Rot(20, 40, 80)`` around all three axes relative to the plane.

3. **Rotate and position an object relative to a location**

    .. code-block:: python

        loc = Location((0.1, 0.2, 0.3), (10, 20, 30))

        face = loc * Rectangle(1,2)

        box = loc *  Rot(20, 40, 80) * Pos(0.2, 0.4, 0.1) * Box(0.2, 0.2, 0.2)

        show_object(face, name="face")
        show_object(location_symbol(loc), name="location")
        show_object(box, name="box")
        show_object(location_symbol(loc *  Rot(20, 40, 80), 0.5), options={"color":(0, 255, 255)}, name="local_location")

    .. image:: assets/location-example-05.png

    The box is positioned via ``Pos(0.2, 0.4, 0.1)`` relative to the location ``loc *  Rot(20, 40, 80)``

4. **Position and rotate an object relative to a location**

    .. code-block:: python

        loc = Location((0.1, 0.2, 0.3), (10, 20, 30))

        face = loc * Rectangle(1,2)

        box = loc * Pos(0.2, 0.4, 0.1) * Rot(20, 40, 80) * Box(0.2, 0.2, 0.2)

        show_object(face, name="face")
        show_object(location_symbol(loc), name="location")
        show_object(box, name="box")
        show_object(location_symbol(loc * Pos(0.2, 0.4, 0.1), 0.5), options={"color":(0, 255, 255)}, name="local_location")

    .. image:: assets/location-example-06.png

    Note: This is the same as `box = loc * Location((0.2, 0.4, 0.1), (20, 40, 80)) * Box(0.2, 0.2, 0.2)`




================================================
FILE: docs/make.bat
================================================
@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd



================================================
FILE: docs/Makefile
================================================
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



================================================
FILE: docs/moving_objects.rst
================================================
Moving Objects
==============

In build123d, there are several methods to move objects. These methods vary 
based on the mode of operation and provide flexibility for object placement 
and orientation. Below, we outline the three main approaches to moving objects: 
builder mode, algebra mode, and direct manipulation methods.

Builder Mode
------------
In builder mode, object locations are defined before the objects themselves are 
created. This approach ensures that objects are positioned correctly during the 
construction process. The following tools are commonly used to specify locations:

1. :class:`~build_common.Locations` Use this to define a specific location for the objects within the `with` block.
2. :class:`~build_common.GridLocations` Arrange objects in a grid pattern.
3. :class:`~build_common.PolarLocations` Position objects in a circular pattern.
4. :class:`~build_common.HexLocations` Arrange objects in a hexagonal grid.

.. note::
   The location(s) of an object must be defined prior to its creation when using builder mode.

Example:

.. code-block:: python

    with Locations((10, 20, 30)):
        Box(5, 5, 5)

Algebra Mode
------------
In algebra mode, object movement is expressed using algebraic operations. The 
:class:`~geometry.Pos` function, short for Position, represents a location, which can be combined 
with objects or planes to define placement.

1. ``Pos() * shape``: Applies a position to a shape.
2. ``Plane() * Pos() * shape``: Combines a plane with a position and applies it to a shape.

Rotation is an important concept in this mode. A :class:`~geometry.Rotation` represents a location 
with orientation values set, which can be used to define a new location or modify 
an existing one.

Example:

.. code-block:: python

    rotated_box = Rotation(45, 0, 0) * box

Direct Manipulation Methods
---------------------------
The following methods allow for direct manipulation of a shape's location and orientation 
after it has been created. These methods offer a mix of absolute and relative transformations.

Position
^^^^^^^^
- **Absolute Position:** Set the position directly.
  
.. code-block:: python

    shape.position = (x, y, z)
  
- **Relative Position:** Adjust the position incrementally.

.. code-block:: python

    shape.position += (x, y, z)
    shape.position -= (x, y, z)
  

Orientation
^^^^^^^^^^^
- **Absolute Orientation:** Set the orientation directly.

.. code-block:: python

      shape.orientation = (X, Y, Z)

- **Relative Orientation:** Adjust the orientation incrementally.

.. code-block:: python

    shape.orientation += (X, Y, Z)
    shape.orientation -= (X, Y, Z)

Movement Methods
^^^^^^^^^^^^^^^^
- **Relative Move:**

.. code-block:: python

    shape.move(Location)
  
- **Relative Move of Copy:**

.. code-block:: python

    relocated_shape = shape.moved(Location)
  
- **Absolute Move:**

.. code-block:: python

    shape.locate(Location)
  
- **Absolute Move of Copy:**

.. code-block:: python

    relocated_shape = shape.located(Location)
  

Transformation a.k.a. Translation and Rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    These methods don't work in the same way as the previous methods in that they don't just change
    the object's internal :class:`~geometry.Location` but transform the base object itself which
    is quite slow and potentially problematic.

- **Translation:** Move a shape relative to its current position.

.. code-block:: python

    relocated_shape = shape.translate(x, y, z)
  
- **Rotation:** Rotate a shape around a specified axis by a given angle.

.. code-block:: python

    rotated_shape = shape.rotate(Axis, angle_in_degrees)



================================================
FILE: docs/objects.rst
================================================
#######
Objects
#######

Objects are Python classes that take parameters as inputs and create 1D, 2D or 3D Shapes.
For example, a :class:`~objects_part.Torus` is defined by a major and minor radii. In
Builder mode, objects are positioned with ``Locations`` while in Algebra mode, objects
are positioned with the ``*`` operator and shown in these examples:

.. code-block:: python

    with BuildPart() as disk:
        with BuildSketch():
            Circle(a)
            with Locations((b, 0.0)):
                Rectangle(c, c, mode=Mode.SUBTRACT)
            with Locations((0, b)):
                Circle(d, mode=Mode.SUBTRACT)
        extrude(amount=c)

.. code-block:: python

    sketch = Circle(a) - Pos(b, 0.0) * Rectangle(c, c) - Pos(0.0, b) * Circle(d)
    disk = extrude(sketch, c)

The following sections describe the 1D, 2D and 3D objects:

Align
-----

2D/Sketch and 3D/Part objects can be aligned relative to themselves, either centered, or justified
right or left of each Axis. The following diagram shows how this alignment works in 2D:

.. image:: assets/align.svg
    :align: center

For example:

.. code-block:: python

    with BuildSketch():
        Circle(1, align=(Align.MIN, Align.MIN))

creates a circle who's minimal X and Y values are on the X and Y axis and is located in the top right corner.
The ``Align`` enum has values: ``MIN``, ``CENTER`` and ``MAX``.

In 3D the ``align`` parameter also contains a Z align value but otherwise works in the same way.

Note that the ``align`` will also accept a single ``Align`` value which will be used on all axes -
as shown here:

.. code-block:: python

    with BuildSketch():
        Circle(1, align=Align.MIN)

Mode
----

With the Builder API the ``mode`` parameter controls how objects are combined with lines, sketches, or parts
under construction.  The ``Mode`` enum has values:

* ``ADD``: fuse this object to the object under construction
* ``SUBTRACT``: cut this object from the object under construction
* ``INTERSECT``: intersect this object with the object under construction
* ``REPLACE``: replace the object under construction with this object
* ``PRIVATE``: don't interact with the object under construction at all

The Algebra API doesn't use the ``mode`` parameter - users combine objects with operators.

1D Objects
----------

The following objects all can be used in BuildLine contexts. Note that
1D objects are not affected by ``Locations`` in Builder mode.

.. grid:: 3

    .. grid-item-card:: :class:`~objects_curve.Airfoil`

        .. image:: assets/example_airfoil.svg

        +++
        Airfoil described by 4 digit NACA profile

    .. grid-item-card:: :class:`~objects_curve.Bezier`

        .. image:: assets/bezier_curve_example.svg

        +++
        Curve defined by control points and weights

    .. grid-item-card:: :class:`~objects_curve.BlendCurve`

        .. image:: assets/example_blend_curve.svg

        +++
        Curve blending curvature of two curves

    .. grid-item-card:: :class:`~objects_curve.CenterArc`

        .. image:: assets/center_arc_example.svg

        +++
        Arc defined by center, radius, & angles

    .. grid-item-card:: :class:`~objects_curve.DoubleTangentArc`

        .. image:: assets/double_tangent_line_example.svg

        +++
        Arc defined by point/tangent pair & other curve

    .. grid-item-card:: :class:`~objects_curve.EllipticalCenterArc`

        .. image:: assets/elliptical_center_arc_example.svg

        +++
        Elliptical arc defined by center,  radii & angles

    .. grid-item-card:: :class:`~objects_curve.FilletPolyline`

        .. image:: assets/filletpolyline_example.svg

        +++
        Polyline with filleted corners defined by pts and radius

    .. grid-item-card:: :class:`~objects_curve.Helix`

        .. image:: assets/helix_example.svg

        +++
        Helix defined pitch, radius and height

    .. grid-item-card:: :class:`~objects_curve.IntersectingLine`

        .. image:: assets/intersecting_line_example.svg

        +++
        Intersecting line defined by start, direction & other line

    .. grid-item-card:: :class:`~objects_curve.JernArc`

        .. image:: assets/jern_arc_example.svg

        +++
        Arc define by start point, tangent, radius and angle

    .. grid-item-card:: :class:`~objects_curve.Line`

        .. image:: assets/line_example.svg

        +++
        Line defined by end points

    .. grid-item-card:: :class:`~objects_curve.PolarLine`

        .. image:: assets/polar_line_example.svg

        +++
        Line defined by start, angle and length

    .. grid-item-card:: :class:`~objects_curve.Polyline`

        .. image:: assets/polyline_example.svg

        +++
        Multiple line segments defined by points

    .. grid-item-card:: :class:`~objects_curve.RadiusArc`

        .. image:: assets/radius_arc_example.svg

        +++
        Arc defined by two points and a radius

    .. grid-item-card:: :class:`~objects_curve.SagittaArc`

        .. image:: assets/sagitta_arc_example.svg

        +++
        Arc defined by two points and a sagitta

    .. grid-item-card:: :class:`~objects_curve.Spline`

        .. image:: assets/spline_example.svg

        +++
        Curve define by points

    .. grid-item-card:: :class:`~objects_curve.TangentArc`

        .. image:: assets/tangent_arc_example.svg

        +++
        Arc defined by two points and a tangent

    .. grid-item-card:: :class:`~objects_curve.ThreePointArc`

        .. image:: assets/three_point_arc_example.svg

        +++
        Arc defined by three points

    .. grid-item-card:: :class:`~objects_curve.ArcArcTangentLine`

        .. image:: assets/example_arc_arc_tangent_line.svg

        +++
        Line tangent defined by two arcs

    .. grid-item-card:: :class:`~objects_curve.ArcArcTangentArc`

        .. image:: assets/example_arc_arc_tangent_arc.svg

        +++
        Arc tangent defined by two arcs

    .. grid-item-card:: :class:`~objects_curve.PointArcTangentLine`

        .. image:: assets/example_point_arc_tangent_line.svg

        +++
        Line tangent defined by a point and arc

    .. grid-item-card:: :class:`~objects_curve.PointArcTangentArc`

        .. image:: assets/example_point_arc_tangent_arc.svg

        +++
        Arc tangent defined by a point, direction, and arc

Reference
^^^^^^^^^
.. py:module:: objects_curve

.. autoclass:: BaseLineObject
.. autoclass:: Airfoil
.. autoclass:: Bezier
.. autoclass:: BlendCurve
.. autoclass:: CenterArc
.. autoclass:: DoubleTangentArc
.. autoclass:: EllipticalCenterArc
.. autoclass:: FilletPolyline
.. autoclass:: Helix
.. autoclass:: IntersectingLine
.. autoclass:: JernArc
.. autoclass:: Line
.. autoclass:: PolarLine
.. autoclass:: Polyline
.. autoclass:: RadiusArc
.. autoclass:: SagittaArc
.. autoclass:: Spline
.. autoclass:: TangentArc
.. autoclass:: ThreePointArc
.. autoclass:: ArcArcTangentLine
.. autoclass:: ArcArcTangentArc
.. image:: assets/objects/arcarctangentarc_keep_table.png
    :alt: ArcArcTangentArc keep table
    :align: center

.. autoclass:: PointArcTangentLine
.. autoclass:: PointArcTangentArc

2D Objects
----------

.. grid:: 3

    .. grid-item-card:: :class:`~drafting.Arrow`

        .. image:: assets/arrow.svg

        +++
        Arrow with head and path for shaft

    .. grid-item-card:: :class:`~drafting.ArrowHead`

        .. image:: assets/arrow_head.svg

        +++
        Arrow head with multiple types


    .. grid-item-card:: :class:`~objects_sketch.Circle`

        .. image:: assets/circle_example.svg

        +++
        Circle defined by radius

    .. grid-item-card:: :class:`~drafting.DimensionLine`

        .. image:: assets/d_line.svg

        +++
        Dimension line


    .. 