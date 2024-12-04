from fast_read_mtx import BatchSampleReader

def test_read():
    reader = BatchSampleReader('/mnt/112-rawdata-112/output/macaque-20241203/')
    adatas = reader.read(verbose=False, with_tqdm=False)

    shapes = {
        adata.uns['sample_name']: adata.shape for adata in adatas
    }
    target_shapes = {
        '105T85-1-210422': (2123, 19194),
        '105T85-2-210422': (1588, 18800),
        '54T37-1-210415': (1353, 18659),
        '54T37-2-210415': (1539, 18957),
        '65T49-1-210416': (1299, 18740),
        '65T49-2-210416': (1351, 18573),
        '68T49-1-210416': (1368, 18607),
        '68T49-2-210416': (1493, 19086),
        '71T61-1-210420': (1650, 18900),
        '71T61-2-210420': (2461, 19405),
        '72T61-1-210420': (1695, 19172),
        '72T61-2-210420': (4517, 19847),
        '79T73-1-210420': (1075, 18712),
        '79T73-2-210420': (2814, 19466),
        '7T35-1-210426': (4162, 19796),
        '7T35-2-210426': (1671, 18730),
        '90T85-1-210421': (1807, 18889),
        '90T85-2-210421': (3958, 20198),
        'MQC286R-159.SZM20230403': (3872, 20283),
        'MQC286R-160.SZM20230403': (3800, 20361),
        'MQC286R-196.SZM20230403': (3993, 20386),
        'MQC286R-197.SZM20230403': (4536, 19918),
        'MQC286R-268.SZM20230403': (8103, 20637),
        'SZM20230529_MQ277L-249': (11243, 21018),
        'SZM20230529_MQ277L-250': (17731, 21697),
        'SZM20230529_MQ277L-510': (16316, 21160),
        'SZM20230529_MQ277L-513': (9166, 20970),
        'ssDNA_97_LC0613': (4347, 20160),
        'ssDNA_98_LC0613': (14475, 21107),
        'ssDNA_107_LC0613': (17834, 21468),
        'ssDNA_94_LC0613': (19106, 21348),
        'ssDNA_95_LC0613': (13515, 20308),
        'ssDNA_33_LZY20230427': (7596, 20958),
        'ssDNA_24_LZY20230427': (3743, 20463),
        'MQC286R-42.SZM20230403': (12647, 21107),
        'SZM20230529_MQ277L-174': (17455, 21205),
        'SZM20230529_MQ277L-219': (3896, 19377),
        '80T73-1-210420': (3544, 19517),
        '80T73-2-210420': (3544, 19517),
    }
    assert len(adatas) == 39
    assert shapes == target_shapes