_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/waymo_769x769.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_160k.py'
]
model = dict(
    decode_head=dict(
        align_corners=True,
        num_classes=28,
        class_weight=[
            8.946727771468966, 2.6460010277330217, 5.25875611511591, 5.421826212633951,
            6.207443117007697, 8.79966021873657, 8.487535420003457, 7.864169908280608,
            5.23090732559429, 8.241533688230493, 10.91879855798167, 11.808081239957763,
            11.317342573968379, 7.992534678092636, 4.676443799157901, 8.897393914998679,
            5.704968559767755, 6.782979693805269, 1.5855578877164693, 1.7305862109401922,
            5.449878906462448, 5.015968360603824, 2.7565977811216706, 1.6086718952170977,
            2.1429179199857527, 2.793024787828894, 5.444033700798115, 2.8614151660636127
        ]),
    auxiliary_head=dict(
        align_corners=True,
        num_classes=28,
        class_weight=[
            8.946727771468966, 2.6460010277330217, 5.25875611511591, 5.421826212633951,
            6.207443117007697, 8.79966021873657, 8.487535420003457, 7.864169908280608,
            5.23090732559429, 8.241533688230493, 10.91879855798167, 11.808081239957763,
            11.317342573968379, 7.992534678092636, 4.676443799157901, 8.897393914998679,
            5.704968559767755, 6.782979693805269, 1.5855578877164693, 1.7305862109401922,
            5.449878906462448, 5.015968360603824, 2.7565977811216706, 1.6086718952170977,
            2.1429179199857527, 2.793024787828894, 5.444033700798115, 2.8614151660636127
        ]))
