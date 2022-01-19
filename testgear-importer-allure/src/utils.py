import re


def form_steps(steps):
    adapt_steps = []
    results_steps = []
    attachments = []
    for step in steps:
        if 'steps' in step:
            inner_steps, inner_results_steps, inner_attachments = form_steps(step['steps'])
            attachments += inner_attachments
        else:
            inner_steps = []
            inner_results_steps = []
        adapt_steps.append(
            {
                'title': step['name'],
                'steps': inner_steps
            }
        )
        results_steps.append(
            {
                'title': step['name'],
                'stepResults': inner_results_steps,
                'outcome': step['status'].title() if step['status'] in ('passed', 'skipped') else 'Failed',
                'duration': step['stop'] - step['start'],
                'parameters': form_parameters(step['parameters']) if 'parameters' in step else None
            }
        )
        if 'attachments' in step:
            attachments += step['attachments']
    return adapt_steps, results_steps, attachments


def form_labels_namespace_classname_workitems_id(allure_labels):
    classname = None
    namespace = None
    labels = []
    workitems_id = []
    for label in allure_labels:
        if label['name'] == 'testcase':
            workitems_id.append(label['value'])
        else:
            labels.append({'name': f"{label['name']}:{label['value']}"})
        if label['name'] == 'package':
            pass
        elif label['name'] == 'subSuite':
            namespace = label['value']
        elif label['name'] == 'testClass':
            namespace = label['value'][label['value'].rfind('.') + 1:]
    return labels, namespace, classname, workitems_id


def form_links(allure_links):
    links = []
    for link in allure_links:
        links.append({})
        if 'url' in link and re.fullmatch(r'^(?:(?:(?:https?|ftp):)?\/\/)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-zA-Z0-9\u00a1-\uffff][a-zA-Z0-9\u00a1-\uffff_-]{0,62})?[a-zA-Z0-9\u00a1-\uffff]\.)+(?:[a-zA-Z\u00a1-\uffff]{2,}\.?))(?::\d{2,5})?(?:[/?#]\S*)?$', link['url']):
            links[-1]['url'] = link['url']
        else:
            raise Exception('Some links have the wrong URL or no URL!')
        if 'type' in link and link['type'] in ('Related', 'BlockedBy', 'Defect', 'Issue', 'Requirement', 'Repository'):
            links[-1]['type'] = link['type']
        if 'name' in link:
            links[-1]['title'] = link['name']
    return links


def form_setup_teardown(data_before_after, uuid):
    setup = []
    teardown = []
    results_setup = []
    results_teardown = []
    attachments = []
    for time in data_before_after:
        for child in data_before_after[time]['children']:
            if child == uuid:
                steps, results_steps, inner_attachments = form_steps(data_before_after[time]['befores'])
                setup += steps
                results_setup += results_steps
                attachments += inner_attachments
                steps, results_steps, inner_attachments = form_steps(data_before_after[time]['afters'])
                teardown += steps
                results_teardown += results_steps
                attachments += inner_attachments
    return setup, results_setup, teardown, results_teardown, attachments


def form_parameters(allure_parameters):
    parameters = {}
    for parameter in allure_parameters:
        parameters[parameter['name']] = parameter['value']
    return parameters
