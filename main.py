from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.initiate_model_training()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e    



# # Another approach to run the pipelines, all from the main file
# # Without creating a seperate pipelines module.
# from src.datascience import logger
# from src.datascience.config.configuration import ConfigurationManager
# from src.datascience.components import (
#     data_ingestion,
#     data_transformation,
#     data_validation,
#     model_trainer,
#     model_evaluation
# )

# class DataIngestionPipeline:
#     def __init__(self):
#         pass

#     def initiate_data_ingestion(self):
#         try:
#             logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#             config = ConfigurationManager()
#             data_ingestion_config = config.get_data_ingestion_config()
#             ingestion = data_ingestion.DataIngestion(config=data_ingestion_config)
#             ingestion.download_file()
#             ingestion.extract_zip()
#             logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
#         except Exception as e:
#             logger.exception(e)
#             raise e


# class DataValidationPipeline:
#     def __init__(self):
#         pass

#     def initiate_data_validation(self):
#         try:
#             logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#             config = ConfigurationManager()
#             data_validation_config = config.get_validation_config()
#             validation = data_validation.DataValidation(config=data_validation_config)
#             validation.validate_all_columns()
#             logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
#         except Exception as e:
#             logger.exception(e)
#             raise e
        

# if __name__=="__main__":

#     STAGE_NAME = "Data Ingestion"
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.initiate_data_ingestion()

#     STAGE_NAME = "Data Validation"
#     data_validation = DataValidationPipeline()
#     data_validation.initiate_data_validation()