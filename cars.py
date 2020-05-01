def car_info(make, model, **options):
	car_dict = {
		'make': make.title(),
		'model': model.title(),
		}
	for option, value in options.items():
		car_dict[option] = value
	return car_dict