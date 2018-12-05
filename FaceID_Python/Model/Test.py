import os, argparse
from FaceID import FaceID
from SampleGenerator import sample_dc, sample_ds

th = 0.5

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', help="Save folder to load")
    args = vars(parser.parse_args())

    save_name = args['save']

    if not save_name:
        save_name = 'model_weigths'

    faceID = FaceID()
    faceID.load(save_name)

    correct_v = 0
    correct_f = 0

    for i in range(50):
        s = sample_dc(True, validation=True)
        if faceID.predict(s, threshold=th):
            correct_v = correct_v + 1;

    for i in range(50):
        s = sample_dc(False, validation=True)
        if not faceID.predict(s, threshold=th):
            correct_f = correct_f + 1;

    print('Correct DC: '+str(correct_v+correct_f)+'/100')
    print('  - Correct pos: '+str(correct_v)+'/50')
    print('  - Correct neg: '+str(correct_f)+'/50')

    correct_v = 0
    correct_f = 0


    for i in range(50):
        s = sample_ds(True, validation=True)
        if faceID.predict(s, threshold=th):
            correct_v = correct_v + 1;

    for i in range(50):
        s = sample_ds(False, validation=True)
        if not faceID.predict(s, threshold=th):
            correct_f = correct_f + 1;

    print('Correct DS: '+str(correct_v+correct_f)+'/100')
    print('  - Correct pos: '+str(correct_v)+'/50')
    print('  - Correct neg: '+str(correct_f)+'/50')
