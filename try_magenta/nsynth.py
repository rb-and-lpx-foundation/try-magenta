from skimage.transform import resize

from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen


class Audio:
    def __init__(
        self, fname, sample_length, sr=16000, ckpt="wavenet-ckpt/model.ckpt-200000"
    ):
        self.fname = fname
        self.sample_length = sample_length
        self.sr = sr
        self.ckpt = ckpt
        self.audio = None
        self.encoding = None

    def load_audio(self):
        self.audio = utils.load_audio(
            self.fname, sample_length=self.sample_length, sr=self.sr
        )

    @property
    def duration(self):
        return self.sample_length / float(self.sr)


class EncodedAudio(Audio):
    def __init__(
        self, fname, sample_length, sr=16000, ckpt="wavenet-ckpt/model.ckpt-200000"
    ):
        Audio.__init__(self, fname, sample_length, sr=sr, ckpt=ckpt)
        self.load_audio()

    def encode(self):
        self.encoding = fastgen.encode(self.audio, self.ckpt, self.sample_length)


class DecodedAudio(Audio):
    def __init__(
        self,
        encoding,
        fname,
        sample_length,
        sr=16000,
        ckpt="wavenet-ckpt/model.ckpt-200000",
    ):
        Audio.__init__(self, fname, sample_length, sr=sr, ckpt=ckpt)
        self.encoding = encoding

    def decode(self):
        fastgen.synthesize(
            self.encoding,
            save_paths=[self.fname],
            checkpoint_path=self.ckpt,
            samples_per_save=self.sample_length,
        )
        self.load_audio()


def timestretch(encoding, factor):
    min_encoding, max_encoding = encoding.min(), encoding.max()
    encodings_norm = (encoding - min_encoding) / (max_encoding - min_encoding)
    timestretches = []
    for encoding_i in encodings_norm:
        stretched = resize(encoding_i, (int(encoding_i.shape[0] * factor), encoding_i.shape[1]), mode='reflect')
        stretched = (stretched * (max_encoding - min_encoding)) + min_encoding
        timestretches.append(stretched)
    return np.array(timestretches)


def decoded_from_encoded(encoded: Audio, fname):
    return DecodedAudio(
        encoded.encoding, fname, encoded.sr, encoded.sample_length, ckpt=encoded.ckpt
    )



