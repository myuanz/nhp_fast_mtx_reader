from fast_mtx_reader import BatchSampleReader

def test_read():
    reader = BatchSampleReader('/mnt/112-rawdata-112/output/macaque-20241203/')
    adatas = reader.read(verbose=False, with_tqdm=False)

    shapes = {
        adata.uns['sample_name']: adata.shape for adata in adatas
    }
    target_shapes = {
        'MQC286R-42.SZM20230403' : (3743, 20463),
        'SZM20230529_MQ277L-174' : (12647, 21107),
    }
    assert shapes == target_shapes
