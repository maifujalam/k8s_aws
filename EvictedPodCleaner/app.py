#!/bin/python3
import kubernetes

if __name__ == '__main__':
    kubernetes.config.load_kube_config()
    v1=kubernetes.client.CoreV1Api()
    pods=v1.list_pod_for_all_namespaces(watch=False)
    count=0
    for pod in pods.items:
        if pod.status.phase != 'Running':
            print(pod.metadata.name+ " | "+pod.metadata.namespace+" | "+pod.status.phase)
        try:
            if pod.status.reason:
                if pod.status.reason == "Evicted":
                    print("Deleting Evicted Pod "+pod.metadata.name)
                    v1.delete_namespaced_pod(pod.metadata.name, pod.metadata.namespace)
                    print("Deleted Evicted Pod "+pod.metadata.name)

        except:
            print("Failed to get pod status")