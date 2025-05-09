from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class Breeam4b(Function):
    """Calculate credits for BREEAM 4b."""

    folder = Inputs.folder(
        description='Path to an output folder of an annual daylight recipe. Folder '
        'should include grids_info.json and sun-up-hours.txt. The command uses the list '
        'in grids_info.json to find the result files for each sensor grid.',
        path='results'
    )

    model = Inputs.file(
        description='Path to HBJSON file. The purpose of the model in this function is '
        'to use the mesh area of the sensor grids to calculate area-weighted metrics. '
        'In case no model is provided or the sensor grids in the model do not have any '
        'mesh area, it will be assumed that all sensor points cover the same area.',
        path='model.hbjson', optional=True
    )

    @command
    def breeam_daylight_4b(self):
        return 'honeybee-radiance-postprocess post-process breeam breeam-4b ' \
            'results --model-file model.hbjson --sub-folder breeam_summary'

    # outputs
    breeam_summary = Outputs.folder(
        description='BREEAM summary folder.',
        path='breeam_summary'
    )
